echo "My first name is $1"
echo "My surname is $2"
echo "Total number of arguments is $#" 
Save this file as name.sh, set execute permission on that file by typing chmod a+x name.sh and then execute the file like this: ./name.sh.

$ chmod a+x name.sh
$ ./name.sh Hans-Wolfgang Loidl
My first name is Hans-Wolfgang
My surname is Loidl
Total number of arguments is 2
Version 1: Line count example
############
Developing specialist knowledge in relevant systems, sharing that knowledge with team members and global partners

#############
http://www.akamaras.com/linux/linux-script-to-check-if-a-service-is-running-and-start-it-if-its-stopped/


############### TCPDUMP
Capture  all  tcp  and  udp  packets  in LAN, except packets coming to localhost (192.168.1.2)
sudo  tcpdump  -n  -i  eth0  -w  data.pcap -v tcp or udp and 'not host

tcpdump into file with date format for wireshark
tcpdump -i eth1 -s0 -v -w /tmp/capture_`date +%d_%m_%Y__%H_%I_%S`.pcap

capture trafic for wireshark from spesific eth interface
tcpdump -i eth1 -s0 -v -w /tmp/capture.pcap


tcpdump top 10 talkers capture 2000 packets and print the top 10 talkers
  tcpdump  -tnn -c 2000 -i eth0 | awk -F "." '{print $1"."$2"."$3"."$4}'
   | sort | uniq -c | sort -nr | awk ' $1 > 10 '

Show header HTTP with tcpdump Where src or dst is the host that you want to view the HTTP header.
tcpdump -s 1024 -l -A src 192.168.9.56 or dst 192.168.9.56

Read  a tcpdump file and count SYN packets to port 80, Order column by
   destination.
tcpdump  -ntr  NAME_OF_CAPTURED_FILE.pcap 'tcp[13] = 0x02 and dst port
   80'  | awk '{print $4}' | tr . ' ' | awk '{print $1"."$2"."$3"."$4}' |
   sort | uniq -c | awk ' {print $2 "\t" $1 }'

ctstat (8)           - unified linux network statistics
ifdown (8)           - take a network interface down
ifup (8)             - bring a network interface up
lft (8)              - print the route packets trace to network host
lft.db (8)           - print the route packets trace to network host
lnstat (8)           - unified linux network statistics
mii-diag (8)         - Network adapter control and monitoring
mtr (8)              - a network diagnostic tool
netstat (8)          - Print network connections, routing tables, interface s..
nmap (1)             - Network exploration tool and security / port scanner
nstat (8)            - network statistics tools.
ping (8)             - send ICMP ECHO_REQUEST to network hosts
ping6 (8)            - send ICMP ECHO_REQUEST to network hosts
rtacct (8)           - network statistics tools.
rtstat (8)           - unified linux network statistics
tcptraceroute (8)    - print the route packets trace to network host
tracepath (8)        - traces path to a network host discovering MTU along th..
.
tracepath6 (8)       - traces path to a network host discovering MTU along th..
traceroute (8)       - print the route packets trace to network host
wget (1)             - The non-interactive network downloader.
wireshark (1)        - Interactively dump and analyze network traffic



grep host jobs kill ping sleep ssh wc
   for  host in $HOSTNAMES; do ping -q -c3 $host && ssh $host 'command' &
   for  count  in  {1..15};  do  sleep  1; jobs | wc -l | grep -q ^0\$ &&
   continue; done; kill %1; done &>/dev/null



tcpdump host 192.168.1.4 and port 31337 -w out 
Explanation: Tcpdump is a traffic analyzer package from Ethereal. The "tcpdump host 192.168.1.4 
and port 31337 -w out" command will give the required information. The -w option will write the 
information to a file rather than display it on screen. 

tcpdump from src to dst then open with wireshark
tcpdump src <srcIP> and dst <dstIP> -w file.pcap

"tcpdump src x.x.x.x or dst x.x.x.x"
      where the x.x.x.x is your client address - and check the outputs - the
      packets will have ports in them.


connected_nodes() 
{
  netstat -an |
  awk '/8333/ && /ESTA/ { print $5 }' |
  sed 's/[.:]8333//'
}



# tcpdump config
IF="-i $DEFAULT"
ASCII="-A"
BINARY="-XX"
NO_DNS="-n"
FULL_PACKETS="-s 0"
NODES=($(connected_nodes))
PORT="8333"
FILE="bitdump.pcap"

#################
# Quick overview of packets, fails, re-trans
		
netstat -i | column -t
		
echo

###################

# The tcpdump command creates a circular buffer of -W X dump files -C YM in size (in MB).

# The default value is 4 files, 256M in size, it is recommended to modify the buffer values
# depending on the capture window needed.


tcpdump="tcpdump -s0 -n -i $interface host $nfs_server_ip -W 4 -C 256 -w $output -Z root"


echo $tcpdump
 echo "Waiting for '$match' to show up in $log"


######### NETSTAT
        let conncount=0

        for p in ${pidlist}
          do
          #let conncount+=`netstat -np 2>/dev/null |grep ${p}/ |wc -l`
          let conncount+=`ls -1 /proc/${p}/fd |wc -l`
        done

#################
--------
ss -inputeam
nc -v -n -z -w 1 87.###.1##.## 80
tcpdump -vn -i any dst port 443
ss -tm src :22 | more
"ss -tm state listening" will show you the drop count per listener.
sysctl -a | egrep tcp..*mem
lsof -PniTCP
ss -nli|fgrep cwnd
ss --options --extended --memory --processes --info




----
 ss -tm
https://patchwork.kernel.org/patch/9908259/

lpaa5:~# ss -tm state listening src :22
Recv-Q Send-Q Local Address:Port                 Peer Address:Port                
0      128             *:ssh                           *:*                    
	 skmem:(r0,rb8388608,t0,tb8388608,f0,w0,o0,bl0,d7)
0      128            :::ssh                          :::*                    
	 skmem:(r0,rb8388608,t0,tb8388608,f0,w0,o0,bl0,d0)

You can see here that the IPv4 listener for ssh had 7 drops.

------
ss -tm
https://patchwork.ozlabs.org/patch/618164/
We have plenty of drop points in the kernel without a message in syslog,
but proper SNMP counter updates.

Look at my recent commit 
9caad864151e525 ("tcp: increment sk_drops for listeners")

"ss -tm state listening" will show you the drop count per listener.
------
ss -tm
https://stackoverflow.com/questions/15265112/can-the-recv-function-receive-more-bytes-than-its-internal-buffer
http://lkml.iu.edu/hypermail/linux/kernel/1207.2/01561.html

------
ss -tm src :22 | more
> From: Eric Dumazet <edumazet@...gle.com>
> 
> SK_MEMINFO_DROPS is added in linux-4.7 for TCP, UDP and SCTP
> 
> skmem will display the socket drop count using d prefix as in :
> 
> $ ss -tm src :22 | more
> State      Recv-Q Send-Q Local Address:Port    Peer Address:Port                
> ESTAB      0      52     10.246.7.151:ssh      172.20.10.101:50759                
> 	 skmem:(r0,rb8388608,t0,tb8388608,f1792,w2304,o0,bl0,d0)
http://lists.openwall.net/netdev/2016/04/22/115
------
allintext:"cubic wscale:"
Using SS tool for network troubleshooting
https://tipstricks.itmatrix.eu/using-ss-tool-for-network-troubleshooting/
https://blog.janestreet.com/inspecting-internal-tcp-state-on-linux/
https://access.redhat.com/solutions/419513
https://access.redhat.com/discussions/782343
https://access.redhat.com/solutions/3126931
https://loicpefferkorn.net/2016/03/linux-network-metrics-why-you-should-use-nstat-instead-of-netstat/
https://unix.stackexchange.com/questions/104976/whats-the-format-spec-for-ss-d
https://qumulo.com/blog/investigating-storage-performance/
https://serverfault.com/questions/720472/sometimes-unable-to-tune-linux-tcp-stack-for-improved-high-latency-performance

https://translate.googleusercontent.com/translate_c?depth=1&hl=en&prev=search&rurl=translate.google.co.uk&sl=zh-CN&sp=nmt4&u=https://github.com/jiacai2050/ideas/issues/41&xid=17259,15700019,15700124,15700149,15700168,15700186,15700190,15700201,15700208&usg=ALkJrhiCVXecOayd3s40A2lLp6d2gKTDNw


------
Allow ss -i to display more TCP informations :

unacked:N   Number of un-acked packets
retrans:X/Y   X: number of outstanding retransmit packets
              Y: total number of retransmits for the session
lost:N       Number of lost packets (tcpi_lost)
sacked:N     Number of sacked packets (tcpi_sacked)
facked:N     Number of facked packets (tcpi_facked)
reordering:N Reordering level (if different of 3)

Example :

$ ss -emoi dst 10.7.7.83
tcp   ESTAB      0      1154056   10.7.7.84:54127    10.7.7.83:34342
timer:(on,200ms,0) ino:57003 sk:ffff88063c51d0c0 <->
	 skmem:(r0,rb89280,t0,tb2097152,f726504,w1436184,o0,bl0) ts sack cubic
wscale:7,6 rto:310 rtt:107.375/1 mss:1448 cwnd:568 ssthresh:108 send
61.3Mbps unacked:568 retrans:0/21 reordering:127 rcv_space:29200
https://patchwork.ozlabs.org/patch/254320/
-------
Analyzing Network Packets with Wireshark, Elasticsearch, and Kibana
https://www.elastic.co/blog/analyzing-network-packets-with-wireshark-elasticsearch-and-kibana
------------


##########

irqstats
http://oliveryang.net/2015/06/python-and-irqstat/
https://github.com/yangoliver/mytools
https://github.com/lanceshelton/irqstat
--------------
MakeDir ${LOGDIR}/network

	$IFCONFIG  -a		> ${LOGDIR}/network/ifconfig_-a.out    2>&1
	$NETSTAT -rn		> ${LOGDIR}/network/netstat_-rn.out    2>&1
	$NETSTAT -lan		> ${LOGDIR}/network/netstat_-lan.out   2>&1
	$NETSTAT -lav		> ${LOGDIR}/network/netstat_-lav.out   2>&1
	$NETSTAT -tulpn		> ${LOGDIR}/network/netstat_-tulpn.out 2>&1
	$NETSTAT -ape		> ${LOGDIR}/network/netstat_-ape.out   2>&1
	$NETSTAT -uan		> ${LOGDIR}/network/netstat_-uan.out   2>&1
	$NETSTAT -s 		> ${LOGDIR}/network/netstat_-s.out     2>&1
	$NETSTAT -in 		> ${LOGDIR}/network/netstat_-in.out    2>&1
	$ROUTE  -nv		> ${LOGDIR}/network/route_-nv.out      2>&1
	$ARP  -a		> ${LOGDIR}/network/arp_-a.out         2>&1

	if [ -x "$IP" ] ; then
		$IP  add	> ${LOGDIR}/network/ip_add.out     2>&1
		$IP  route	> ${LOGDIR}/network/ip_route.out   2>&1
		$IP  link	> ${LOGDIR}/network/ip_link.out    2>&1
		$IP  rule	> ${LOGDIR}/network/ip_rule.out    2>&1
	fi

--------------------
x:\pytontest\sh-files\netstat-2254.sh
************************************************************************
iNum="5400"
while [ "$iNum" -ge "0" ]
do
EST_CONNS=`netstat -an |grep "10.53.126.14" |grep "ESTABLISHED" |wc -l`
TW_CONNS=`netstat -an |grep "10.53.126.14" |grep "TIME_WAIT" |wc -l`
CL_CONNS=`netstat -an |grep "10.53.126.14" |grep "CLOSED" |wc -l`
FW_CONNS=`netstat -an |grep "10.53.126.14" |grep "FIN_WAIT" |wc -l`
CW_CONNS=`netstat -an |grep "10.53.126.14" |grep "CLOSE_WAIT" |wc -l`
echo "$1 - 10.53.126.14  | " `date` " | EST="$EST_CONNS" | TW="$TW_CONNS" | CL="$CL_CONNS" | FW="$FW_CONNS" | CW="$CW_CONNS >>Netstat_$1.log
EST_CONNS=`netstat -an |grep "10.53.126.12" |grep "ESTABLISHED" |wc -l`
TW_CONNS=`netstat -an |grep "10.53.126.12" |grep "TIME_WAIT" |wc -l`
CL_CONNS=`netstat -an |grep "10.53.126.12" |grep "CLOSED" |wc -l`
FW_CONNS=`netstat -an |grep "10.53.126.12" |grep "FIN_WAIT" |wc -l`
CW_CONNS=`netstat -an |grep "10.53.126.12" |grep "CLOSE_WAIT" |wc -l`
echo "$1 - 10.53.126.12  | " `date` " | EST="$EST_CONNS" | TW="$TW_CONNS" | CL="$CL_CONNS" | FW="$FW_CONNS" | CW="$CW_CONNS >> Netstat_$1.log
sleep 2
iNum=`expr $iNum - 1`
done


##########
##########
The general planning steps are:

Define the exact problem situation
Determine optimum capture locations and collect link characteristics
Adjust capture location selection based on available resources


1. Define the problem situation
Connection problems (can’t establish, premature abort, fatal crash)
Critical/unexpected delays, slow response times (write down if you’re talking about seconds, milliseconds, microseconds)
Application problems

2. Determine optimum capture locations
There are usually three sources you may have access to to gather and deploy capture equipment:

servers (JPM & DeShaw)
network device (JPM)
capture locations: both peer points

3. Adjust capture location based on available resources
Start all capture devices before you run the scenarios and stop them after everything is finished
Start and stop the capture before and after each scenario
You need someone to operate the capture devices in each location
Starting and stopping the capture needs to be synchronized, usually via phone calls 
define a capture file naming scheme beforehand 
The most critical thing is to make sure no scenario is started before the capture device operators all signal they’re “good to go, capturing is running”.

################
The general planning steps are:

1. Problem / Situation
Connection problems - Client not receiving SYN packets

2. Capture locations

servers (client 1 & client 2)
network device (client 1 & client 2)
capture locations: both peer points

3. Packet capture setup
src & dest IP address
Start all capture devices before running scenarios and stop them after scenario is finished
Synchronizing starting and stopping the capture e.g via phone calls 
Capture file naming scheme beforehand 