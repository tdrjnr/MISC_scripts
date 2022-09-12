#!/bin/bash
#run-on dbserver.mysite.com frontend.mysite.com 'date; df -h /tmp'
if [ $# = 0 ]
then
	self=`basename $0`
	echo "Execute a command on multiple servers."
	echo
	echo "1. Basic Usage"
	echo
	echo "   $self server1 [server2 ...] command"
	echo
	echo "2. Command"
	echo
	echo "   Keep in mind that the command you want to run should be the last argument"
	echo "   and should be in single or double quotes."
	echo
	echo "3. Remote User"
	echo
	echo "   The commands are ran as root. If you want to run them as another user, use:"
	echo
	echo "   user=www-data $self server1 [server2 ...] command"
	echo
	echo "3. Common Domains"
	echo
	echo "   If all servers are under the same domain, you can set a domain variable and"
	echo "   provide only the subdomain parts to the $self command, like so:"
	echo
	echo "   domain=example.org $self s01 s02 s03 command"
	echo
	echo "   The command will be run on s01.example.org, s02.example.org, and so on."

	exit 1
fi

command="${@: -1}"
servers_count=$(($# - 1))
servers="${@:1:$servers_count}"
user=${user:-root}

if [ -n "$domain" ]
then
	domain=".$domain"
else
	domain=""
fi

if [ -z "$command" ]
then
	echo "Please provide a command to run as the last argument (in quotes)."
	exit 2
fi

if [ -z "$servers" ]
then
	echo "Please provide at least one server name to run the command on."
	exit 3
fi

echo "Running the following command on $servers_count server(s):"
echo
echo $command
echo

for server in $servers
do
	hostname="$server$domain"
	echo "---> Running command on $hostname as $user:"
	ssh $user@$hostname "$command"
	echo
done