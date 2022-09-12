#!/bin/bash

#echo "
#####################################################################
#CPU USAGE
#####################################################################
#"
#printf "%-20s%-20s%-20s\n" "CPU ID" "IDLE" "TOTAL IDLE"
#printf "%-20s%-20s%-20s\n" "------" "----" "---------"

#echo "
#---------------------------------------------------------------------
#Process CPU Usage Detail
#---------------------------------------------------------------------
#"
#printf "%-20s %-20s %-20s %-20s\n" "%CPU" "PID" "USER" "COMMAND"
#ps -ef -o pcpu,pid,user,args|sort -nr|head -10|grep -v "PID"|awk '{ printf "%-20s %-20s %-20s %-20s\n", $1, $2, $3, $4}'

#set -x



#servers=`cat /root/servers.txt`
servers_count=$(cat /root/servers.txt)
servers_count=$(cat /root/servers.txt)
echo $servers_count
for server in $servers_count
do
	echo "Uptime : `uptime -p`"
	#hostname="$server$domain"
	#echo "---> Running command on $hostname as $user:"
	#ssh $user@$hostname "$command"
	ping -c2 $server
	echo $servers
done

