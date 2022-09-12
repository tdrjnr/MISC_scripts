#!/usr/bin/bash
set -x

LOGDIR=.
echo -n "Gathering network info "
mkdir $LOGDIR/network
mkdir $LOGDIR/network/interfaces
iptables --list > $LOGDIR/network/iptables.out 2>&1
ifconfig -a     > $LOGDIR/network/ifconfig.out 2>&1
ip addr show    > $LOGDIR/network/ipaddrshow.out 2>&1
ip -s link show > $LOGDIR/network/iplinkshow.out 2>&1
ss -a           > $LOGDIR/network/ss-s.out 2>&1
netstat -rn     > $LOGDIR/network/netstat.out
ip route        > $LOGDIR/network/ip-route.out 2>&1

which ethtool > /dev/null 2>&1
if [ $? -eq 0 ]
then
   #ALLfaces=`ifconfig -a | grep HW | cut -d" " -f1`
   ALLfaces=`ip addr sh | cut -d" " -f2 | cut -d":" -f1`
   for file in $ALLfaces
   do
      if [ $? -eq 0 ]
      then
         ethtool -S $file > $LOGDIR/network/interfaces/ethtool-S.$file 2>&1
         ethtool    $file > $LOGDIR/network/interfaces/ethtool.$file 2>&1
         ethtool -k $file > $LOGDIR/network/interfaces/ethtool-k.$file 2>&1
         ethtool -i $file > $LOGDIR/network/interfaces/ethtool-i.$file 2>&1
         ethtool -a $file > $LOGDIR/network/interfaces/ethtool-a.$file 2>&1
         ifconfig   $file > $LOGDIR/network/interfaces/ifconfig.$file 2>&1
      fi
   done
fi

echo "... done"