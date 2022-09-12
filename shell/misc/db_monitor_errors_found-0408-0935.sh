#!/bin/bash

# $Id$

###############################################################################
#
# db_monitor_errors_found.sh
#
# This scripts checks all hosts in serch for logged database errors.  It then
# stores findings into the database.
#
###############################################################################

###############################################################################
#
# FUNCTIONS
#
###############################################################################

#
# This cleans up and exits the script.
#
exitScript()
{
  # Read exit code to use.
  ERROR_CODE=${1}

  # Cleanup
  rm -rf ${WORKING_DIR}

  # Exit
  exit ${ERROR_CODE} 
}


###############################################################################
#
# SCRIPT
#
###############################################################################

# Defaults.
TODAY=`date +\%Y-\%m-\%d`
DEPLOYMENT_DB_NAME="deployment"
DEPLOYMENT_DB_USER="helios"
DEPLOYMENT_DB_HOST="heliosdb1"
DB_NAME="helios"
DB_USER="helios"
DB_HOST="heliosdb1"
DB_LOG_DIR="${PWD}"
PAUSE_IN_SECONDS=60
RECEPIENT_LIST="us_support@suntradingllc.com"
SSH_OPTIONS="-o BatchMode=yes -o ConnectTimeout=30 -o StrictHostKeyChecking=no"
ERRORS_REPORT_GENERATOR="${HELIOS_SCRIPT_DIR}/db_monitor_errors_repgen.sh"

# Check for option parameters.
while getopts ":d:U:h:l:T:?" opt
do
  case $opt in
    d )  DB_NAME=${OPTARG} ;;
    U )  DB_USER=${OPTARG} ;;
    h )  DB_HOST=${OPTARG} ;;
    l )  DB_LOG_DIR=${OPTARG} ;;
    T )  RECEPIENT_LIST=${OPTARG} ;;
    ? )  echo "usage: ${0} [-d <database name> -U <database user>"
         echo "             -h <database host> -l <logs directory>"
         echo "             -T <e-mail address>]"
         exitScript 0 ;;
  esac
done

# Determine where to write logs.
ERRORS_LOG_FILE="${DB_LOG_DIR}/database_errors_found.csv"
WORKING_DIR="${DB_LOG_DIR}/check_for_db_errors_${$}"
DB_HOST_LIST="${WORKING_DIR}/hosts_list.txt"
DB_ERRORS_FILE="${WORKING_DIR}/db_errors.log"
ACCESS_ERRORS_FILE="${WORKING_DIR}/access_errors.log"
EMAIL_MESSAGE_FILE="${WORKING_DIR}/e-mail_message.txt"
EMAIL_ERROR_MESSAGE_FILE="${WORKING_DIR}/e-mail_error_message.txt"
ERRORS_FOUND_FILE="${WORKING_DIR}/errors_found_in_hosts.txt"
DB_UPDATE_STATEMENT_FILE="${WORKING_DIR}/db_update.sql"
DB_UPDATE_OUTPUT_FILE="${WORKING_DIR}/db_update_output.log"
DB_UPDATE_ERRORS_FILE="${WORKING_DIR}/db_update_errors.log"

# Create working directory.
if [[ -d ${WORKING_DIR} ]]
then
  rm -rf ${WORKING_DIR}
fi
mkdir ${WORKING_DIR}

# Determine query to use to get host list.
CHECK_QUERY="                                       \
             SELECT DISTINCT user_id || '@' || host \
             FROM job_control                       \
             WHERE enabled                          \
             ORDER BY 1;"

# Execute query.
psql -d ${DB_NAME} -U ${DB_USER} -h ${DB_HOST} -c "${CHECK_QUERY}" -t -o ${DB_HOST_LIST}.tmp 2>${DB_ERRORS_FILE}

# Check for errors.
DB_ERROR_COUNT=`wc -l ${DB_ERRORS_FILE} | cut -d" " -f1`
if [[ ${DB_ERROR_COUNT} -ne 0 ]]
then
  # Prepare error message.
  {
    echo "ERROR: Problems attempting to read host list from \"${DB_NAME}\" on ${DB_USER}@${DB_HOST}."
    echo
    echo "QUERY ATTEMPTED:"
    echo "${CHECK_QUERY}"
    echo
    echo "DATABASE ERROR:"
    cat ${DB_ERRORS_FILE}
  } > ${EMAIL_ERROR_MESSAGE_FILE}

  # Send error e-mail.
  mail -s "DB MONITOR: Error while trying to read host list." "${RECEPIENT_LIST}" < ${EMAIL_ERROR_MESSAGE_FILE}

  # Clean up and exit script.
  exitScript 1
else
  # Cleanup list.
  sed "/^$/d" ${DB_HOST_LIST}.tmp | sed "s/ //g" > ${DB_HOST_LIST}
  rm ${DB_HOST_LIST}.tmp
fi

# Access each host in list.
while read USERHOST
do
  # Write the host to attempt to access error log.
  echo -n "${USERHOST}: " >> ${ACCESS_ERRORS_FILE}

  # Collect error information from host.
  (ssh ${SSH_OPTIONS} ${USERHOST} "grep '^${TODAY}.*DB Err' logs.*/*/current | grep -v hsHeartbeat" >> ${ERRORS_FOUND_FILE} 2>>${ACCESS_ERRORS_FILE} &)

  # Give it some time to finish.
  sleep 1

  # Line terminator.
  echo " ">> ${ACCESS_ERRORS_FILE}
done < ${DB_HOST_LIST}

# Calculate number of errors found.
NUMBER_OF_ERRORS=`cat ${ERRORS_FOUND_FILE} | wc -l`

# Write errors if any found.
if [[ ${NUMBER_OF_ERRORS} -ne 0 ]]
then
  # Initialize database update file.
  echo "BEGIN;" > ${DB_UPDATE_STATEMENT_FILE}

  # Initialize errors log file.
  echo "hostname,process name,jid,time stamp,error message" > ${ERRORS_LOG_FILE}

  # Analyze error found.
  while read WHOLE_LINE
  do
    FIRST_CUT=${WHOLE_LINE%%/*}
    HOST_NAME=${FIRST_CUT#*.}
    FIRST_CUT=${WHOLE_LINE%%/current:*}
    SECOND_CUT=${FIRST_CUT##*/}
    PROCESS=${SECOND_CUT#*.}
    JID=${SECOND_CUT%%.*}
    FIRST_CUT=${WHOLE_LINE#*:}
    TIME_AND_DATE=${FIRST_CUT%% DB Error:*}
    ERROR_MESSAGE=${WHOLE_LINE#* * }

    # Write to a clean logfile
    echo "${HOST_NAME},${PROCESS},${JID},${TIME_AND_DATE},\"${ERROR_MESSAGE}\"" >> ${ERRORS_LOG_FILE}

    # Write results to database.
    echo "INSERT INTO db_monitor_errors_found VALUES('${HOST_NAME}','${PROCESS}',${JID},'${TIME_AND_DATE}','${ERROR_MESSAGE}','${DB_NAME}','${DB_USER}','${DB_HOST}');" >> ${DB_UPDATE_STATEMENT_FILE}
  done < ${ERRORS_FOUND_FILE}

  # Close database update file.
  echo "COMMIT;" >> ${DB_UPDATE_STATEMENT_FILE}

  # Update database with errors found information.
  psql -d ${DEPLOYMENT_DB_NAME} -U ${DEPLOYMENT_DB_USER} -h ${DEPLOYMENT_DB_HOST} -f ${DB_UPDATE_STATEMENT_FILE} -o ${DB_UPDATE_OUTPUT_FILE} 2>${DB_UPDATE_ERRORS_FILE}

  # Check for errors.
  DB_ERROR_COUNT=`wc -l ${DB_UPDATE_ERRORS_FILE} | cut -d" " -f1`
  if [[ ${DB_ERROR_COUNT} -ne 0 ]]
  then
    # Prepare error message.
    {
      echo "ERROR: Problems attempting to write error information into database \"${DEPLOYMENT_DB_NAME}\" on ${DEPLOYMENT_DB_USER}@${DEPLOYMENT_DB_HOST}."
      echo
      echo "QUERY ATTEMPTED:"
      cat ${DB_UPDATE_STATEMENT_FILE}
      echo
      echo "DATABASE ERROR:"
      cat ${DB_UPDATE_ERRORS_FILE}
    } > ${EMAIL_ERROR_MESSAGE_FILE}

    # Send error e-mail.
    mail -s "DB MONITOR: Error while trying to write error information into database." "${RECEPIENT_LIST}" < ${EMAIL_ERROR_MESSAGE_FILE}

    # Clean up and exit script.
    exitScript 1
  fi

  # Cleanup access errors file (preparing for e-mail).
  dos2unix -q -n ${ACCESS_ERRORS_FILE} ${ACCESS_ERRORS_FILE}.tmp
  grep -v ".*:  $" ${ACCESS_ERRORS_FILE}.tmp > ${ACCESS_ERRORS_FILE}
  rm ${ACCESS_ERRORS_FILE}.tmp

  # E-mail results.
  {
    echo "There were ${NUMBER_OF_ERRORS} errors found in the ${DB_NAME} system."
    echo
    cat ${ERRORS_LOG_FILE} | sed "s/,/ /g"

    # If there were access errors, e-mail them too.
    if [[ -s ${ACCESS_ERRORS_FILE} ]]
    then
      echo
      echo
      echo "There were errors while trying to access some hosts:"
      echo
      cat ${ACCESS_ERRORS_FILE}
    fi
  } > ${EMAIL_MESSAGE_FILE}

  # Send results e-mail.
  mail -s "DB MONITOR: ${NUMBER_OF_ERRORS} database errors found. (${DB_NAME} ${DB_USER}@${DB_HOST})" "${RECEPIENT_LIST}" < ${EMAIL_MESSAGE_FILE}
fi

# Generate report.
${ERRORS_REPORT_GENERATOR} -d ${DB_NAME} -U ${DB_USER} -h ${DB_HOST} -T "${RECEPIENT_LIST}"

# Finish.
exitScript 0
