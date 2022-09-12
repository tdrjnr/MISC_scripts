#! /bin/ksh
pid=$1
(( cnt=1000 ))
while [[ $cnt -gt 0 ]];
do
date
pmap -x $pid
#pstack $pid
top -b -p $pid -n 1
echo $cnt
(( cnt=cnt-1 ))
sleep 2
done