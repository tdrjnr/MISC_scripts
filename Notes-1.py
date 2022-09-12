SRE
###
In Troubleshoot search
TCP_NODELAY socket options causes the data from the second write
The moral of the story
So, game over
Tcp would wait for up to 200 milli
within the constraints of the sliding window
A user application can disable the nagle algorithm
Socket buffers and bandwidth delay product

###
tcp_low_latency - BOOLEAN
/proc/sys/net/ipv4/tcp_low_latency
###
strace tcpdump

For a socket, this is probably either connect if that process is a client or accept

strace $(pgrep httpd | sed -e 's/^/-p /')
strace -f -s1000 -p 56899 -e 'trace=!clock_gettime,futex,select
strace -tt -o ${filename} -e trace=network 
gdb --args ${EXECUTABLE}
strace -o out -y cp ubuntu-16.04-desktop-amd64.iso /tmp/blah 
strace -yy wget blah.com
ls -l /proc/$(pidof server)/fd


https://jvns.ca/blog/2016/06/07/strace-y/
https://www.digitalocean.com/community/tutorials/how-to-audit-network-traffic-in-a-lamp-server-with-sysdig-on-centos-7
http://www.informit.com/articles/article.aspx?p=2161291

https://bunn.cc/2017/connection-refused/
https://www.flagword.net/2016/05/have-stalled-snmpd-in-recvfrom-check-recv-q/
https://www.google.co.uk/amp/s/linux-audit.com/the-ultimate-strace-cheat-sheet/amp/
https://gist.github.com/graste/929bb122c353bdd90c20
https://unix.stackexchange.com/questions/16300/whos-got-the-other-end-of-this-unix-socketpair

https://blogs.technet.microsoft.com/yongrhee/2012/12/20/network-tracing-packet-sniffing-data-to-provide-when-troubleshooting/

https://blog.packet-foo.com/2018/01/the-network-capture-playbook-part-6-planning-network-troubleshooting/
###
Syn_ack

http://bl0rg.krunch.be/nfs-perfs.html

###
IRQ Throughout vs latency ftrace irq

irqbalance --oneshot
- static tracepoints

https://www.slideshare.net/mobile/jboner/scalability-availability-stability-patterns/13-TradeoffsPerformance_vs_ScalabilityLatency_vs_ThroughputAvailability

https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_MRG/1.3/html/Realtime_Tuning_Guide/sect-Realtime_Tuning_Guide-Realtime_Specific_Tuning-Using_the_ftrace_Utility_for_Tracing_Latencies.html

https://stackoverflow.com/questions/24207371/linux-kernel-ftrace-irqsoff-tracer-generates-strange-output
http://pyeh.github.io/blog/2014/10/07/notes-of-debugging-the-kernel-using-ftrace/

###
Packet loss
dropwatch
ss -ti
tracedump
----------
https://jvns.ca/blog/2017/09/05/finding-out-where-packets-are-being-dropped/

http://www.draconyx.net/articles/net_drop_monitor-monitoring-packet-loss-in-the-linux-kernel.html
https://stackoverflow.com/questions/8987926/how-to-find-which-packets-got-dropped
https://serverfault.com/questions/214520/how-to-measure-and-minimize-udp-packet-loss

good
https://opensourceforu.com/2016/10/network-performance-monitoring/
###
Python dashboards
http://moderndata.plot.ly/create-a-plotly-dashboards-in-under-10-minutes/
https://blog.sicara.com/bokeh-dash-best-dashboard-framework-python-shiny-alternative-c5b576375f7f
https://assemblinganalytics.com/post/building-a-web-dashboard-with-postgres-python-and-plotly/
https://superset.incubator.apache.org/tutorial.html

https://shuaiw.github.io/2017/08/26/building-beautiful-dashboards-with-superset.html

###
Python refactor
http://docs.python-guide.org/en/latest/writing/style/
http://blog.thedigitalcatonline.com/blog/2017/07/21/refactoring-with-test-in-python-a-practical-example/
https://stackoverflow.com/questions/40695241/refactoring-for-loops-in-python
https://stackoverflow.com/questions/1280667/in-python-is-there-an-easier-way-to-write-6-nested-for-loops/1280724
https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf
http://benlopatin.com/python-refactoring-with-comprehensions/
http://benlopatin.com/posts/
http://blog.cdleary.com/2008/10/idiomatic-python-refactoring-for-else-in-contains-operator/

###
Kafka producer & consume subscriber
https://stackoverflow.com/questions/20520492/how-to-minimize-the-latency-involved-in-kafka-messaging-framework

https://bravenewgeek.com/benchmarking-message-queue-latency/
https://engineering.linkedin.com/kafka/benchmarking-apache-kafka-2-million-writes-second-three-cheap-machines

https://github.com/jkreps/kafka/tree/trunk/bin
http://grokbase.com/t/kafka/users/14cx68zef2/latency-how-to-reduce
https://signalfx.com/blog/how-we-monitor-and-run-kafka-at-scale/



###
/dev/shm
https://superuser.com/questions/396696/debugging-linux-i-o-latency


such as tmpfs or /dev/shm), dd will make system calls to perform the operation, which brings additional costs.

The context switching even in shm is not going anywhere
####

Check process
https://stackoverflow.com/questions/20162678/linux-script-to-check-if-process-is-running-act-on-the-result

https://unix.stackexchange.com/questions/157133/how-to-get-the-pid-of-a-process-and-invoke-kill-9-on-it-in-the-shell-script
####
high swap
https://www.google.co.uk/amp/s/www.cyberciti.biz/faq/linux-which-process-is-using-swap/amp/

https://serverfault.com/questions/377636/swap-95-but-a-lot-of-free-ram-memory

https://www.linuxquestions.org/questions/linux-server-73/100-swap-usage-with-loads-of-free-memory-849452/

https://stackoverflow.com/questions/479953/how-to-find-out-which-processes-are-using-swap-space-in-linux

https://stackpointer.io/unix/linux-swap-usage-per-process/379/
https://unix.stackexchange.com/questions/271765/machine-freezes-once-it-hits-swap-space-under-heavy-load

https://access.redhat.com/solutions/45412
###
Slab
http://collectl.sourceforge.net/SlabInfo.html
http://docs.zephyrproject.org/kernel/memory/slabs.html
###
2.1.1.
Run Queue Statistics
#####
Interfaces

https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python

http://www.shallowsky.com/software/netscheme/netutils-1.4.html


https://github.com/nwhalen/python-iproute2

http://www.fos.tech/posts/pyroute2-linux-networking-made-easy/
#######
How to Pass Arguments to a Bash-Script
https://www.lifewire.com/pass-arguments-to-bash-script-2200571

https://ryanstutorials.net/bash-scripting-tutorial/bash-variables.php
#####
Is there a diagram of the fx landscape on our connectivity to the venues e.g. feedhandlers, algo containers, SOR.
This will help us build a mental picture of the fx landscape when there are issues to better help you guys.

#####
How can I delete a trailing newline in bash?

https://www.novell.com/support/kb/doc.php?id=7014821

https://www.krenger.ch/blog/bash-here-document-at-line-n-delimited-by-end-of-file-wanted-eof/

https://unix.stackexchange.com/questions/140727/how-can-i-delete-a-trailing-newline-in-bash

https://stackoverflow.com/questions/16365155/removing-a-newline-character-at-the-end-of-a-file

https://www.unix.com/shell-programming-and-scripting/182237-how-remove-new-line-character-end-file.html

https://www.qualitestgroup.com/resources/knowledge-center/how-to-guide/remove-windows-carriage-returns-text-files-linux/
#####
/dev/shm

http://517sou.net/archives/understanding-virtual-memory/

https://serverfault.com/questions/590124/performance-difference-between-ramfs-and-tmpfs
https://serverfault.com/questions/590124/performance-difference-between-ramfs-and-tmpfs
https://stackoverflow.com/questions/42884087/how-and-when-to-use-dev-shm-for-efficiency
http://www.pc-freak.net/files/tmpfs.txt

https://www.google.co.uk/amp/www.pc-freak.net/blog/how-to-mount-directory-in-memory-on-gnu-linux-and-freebsd-mount-directory-in-ram-memory-to-increase-performance-on-linux-and-bsd/amp/
https://forum.gitlab.com/t/performance-issues-when-writing-to-tmpfs-during-a-docker-based-gitlab-ci-build/5398/6
https://stackoverflow.com/questions/13370683/linux-3-2-dev-shm-performance-variable
https://www.google.co.uk/amp/s/rwmj.wordpress.com/2012/09/12/tmpfs-considered-harmful/amp/

https://access.redhat.com/discussions/3072191

https://serverfault.com/questions/445445/tmpfs-fills-up-although-hardly-used-how-can-i-debug-this
/var

https://askubuntu.com/questions/140014/how-to-decompress-20gb-of-files-tmpfs-keeps-filling-up

https://engineering.linkedin.com/blog/2016/02/eliminating-large-jvm-gc-pauses-caused-by-background-io-traffic


######
Disk
https://stackoverflow.com/questions/34842735/python-script-to-verify-disk-space-output-from-linux

####
Generators
http://dvalts.io/code/optimisation/2017/08/10/Generators-or-Listcomps.html
####

https://ubuntuforums.org/showthread.php?t=1698757
http://dvalts.io/linux/2018/01/15/Disk-usage-linux.html
#####
Process thread synchronisation
http://pages.cs.wisc.edu/~sschang/OS-Qual/process/process_and_synchronization.htm

https://stackoverflow.com/questions/39185134/how-are-user-level-threads-scheduled-created-and-how-are-kernel-level-threads-c/39185831
#####
Top Directories and Files (Disk Space) in Linux
https://www.google.co.uk/amp/s/www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/amp/

Top 5 Folders Consuming The Most Space?
https://stackoverflow.com/questions/6748791/top-5-folders-consuming-the-most-space

https://serverfault.com/questions/25043/find-largest-directories-files-recursively
#####
check processes
https://www.linuxquestions.org/questions/programming-9/help-with-script-to-check-processes-on-multiple-servers-640817/

https://stackoverflow.com/questions/13330848/bash-script-to-check-multiple-running-processes

https://www.ostechnix.com/find-long-process-running-linux/

https://askubuntu.com/questions/157779/how-to-determine-whether-a-process-is-running-or-not-and-make-use-it-to-make-a-c

In python
https://stackoverflow.com/questions/788411/check-to-see-if-python-script-is-running
https://stackoverflow.com/questions/38056/how-do-you-check-in-linux-with-python-if-a-process-is-still-running
https://www.saltycrane.com/blog/2010/02/hack-copy-files-between-two-remote-hosts-using-python/
#####

#####

#####

#####

#####

#####
Buffer cache sar -b
https://docs.oracle.com/cd/E19620-01/805-4448/6j47cnj0u/index.html
#####

####
Heartbeat interval specified in logon message
Disconnecting the session what are the upstream effects. Are you getting canceled orders and once the connected back are you then receiving the canceled orders etc

Are you getting logour messages upon yhe connection closing
####
There should be enough collaboration that something that  you become very familiar over time somebody else has built, and yes, , but I can't possibly know it as well as the people who built it, right

Heartbeat required to maintain fix connection and drop copies

The heartbeat and test request were not responded to my the client application and was disconnected and took down the venue session.

Fix session heartbeat interval is 60sec but this can be changed by the client

Verify you are receiving heartbeats per instruments

Default heartbeat is 30sec
####
