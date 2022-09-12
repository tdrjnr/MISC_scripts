#!/bin/bash -x

DATE=$(/bin/date +%y%m%d_%H%M%S)
#GZREGEX="s/(.*).gz$/\$1-$DATE_$TIME.gz/"

SRC_DIR=$(dirname $0)
mkdir -p $SRC_DIR/logs
for collector in $(find $SRC_DIR/collectors -executable ! -type d)
do
	collector_name=$(basename $collector)
	log_file=$SRC_DIR/logs/$collector_name
	{
		date +"%F %T" >>$log_file-$DATE
		$collector &>>$log_file-$DATE
		date +"%F %T" >>$log_file-$DATE
		#mv $log_file-$DATE $log_file-$DATE_$TIME
		gzip -f $log_file-$DATE
	} &
done

wait