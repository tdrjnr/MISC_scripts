The third important item that this section tells us is that the packet being sent is a SYN packet. We can
identify this via the Flags [S] section of the snippet. Each line in tcpdump output will have a
section for flags. When the flags set on a packet are only S, this means that the packet is the initial
SYN packet.
 
The fact that this packet is a SYN packet actually tells us quite a bit about the packet.
A quick primer on TCP
 
Transmission Control Protocol (TCP) is one of the most utilized protocols for Internet-based
communications. It is the protocol of choice for many of the services that we rely on every day. From
the HTTP protocol for loading web pages to the favorite of all Linux systems administrators, SSH,
these protocols are implemented on top of the TCP protocol.
 
While TCP is highly used, it is also a rather advanced topic, a topic that every systems administrator
should have at least a basic understanding of. In this section, we are going to quickly cover some TCP
basics; this will by no means be an extensive guide but is just enough to understand the root of our
issue.
 
To understand our issue, we must first understand how TCP connections are established. With TCP
communications, there are generally two important parties, namely the client and the server. The
client is the initiator of the connection and will send a SYN packet as the first step to establishing a
TCP connection.
 
When the server receives a SYN packet and is willing to accept the connection, it will send a
Synchronize Acknowledgement (SYN-ACK) packet back to the client. This is designed for the
server to acknowledge that it has received the original SYN packet.
 
When the client receives this SYN-ACK packet, it then replies to the server with an ACK, sometimes
referred to as a SYN-ACK-ACK. The idea behind this packet is for the client to acknowledge that it has
received the server's acknowledgement.
 
www.hellodigi.ir
---------------------Page 207---------------------
 
This process is known as the Three-Way Handshake and is the foundation of TCP. The benefit of this
method is that, with each system acknowledging the packets that it receives, there is no question as to
whether the client and the server are able to communicate back and forth. Once a three-way
handshake has been performed, the connection is moved to an established state. This is where other
types of packets can be used, such as P us h                 (P S H) packets, which are used to transfer information
from the client to the server or vice versa.
Types of TCP packet
 
Speaking of additional types of packets, it is important to know that the component that defines
whether a packet is a SYN packet or an ACK packet is simply a flag being set in the packet header.
 
On the first packet from our captured data, only the SYN flag is set; this is why we will see output such
as Flags [S]. This is an example of the first packet being sent and that packet having only the SYN
flag set.
 
A  n  SYN-ACK packet is a packet where the SYN and the ACK flags are set. This is commonly seen as
[S.] in tcpdump.
 
The following is a table of packet flags commonly seen during troubleshooting activities with
tcpdump. This is by no means a full list, but it does give a general idea of the common packet types.
  SYN- [S]: This is a Synchronize packet, the first packet sent from the client to the server.
  SYN-ACK- [S.]: This is a Synchronize Acknowledgement packet; these packet flags are used to
  indicate that the server received the client's SYN requests.
  ACK- [.]: The Acknowledgement packet is used by both the server and the client to
  acknowledge the received packets. After the initial SYN packet is sent, all subsequent packets
  should have the acknowledgement flag set.
  PSH- [P]: This is a Push packet. It is designed to push the buffered network data to the receiver.
  This is the type of packet where data is actually transferred.
  PSH-ACK- [P.]: The Push Acknowledgement packet is used to both acknowledge a previous
  packet and send data to the recipient.
  FIN- [F]: The FIN or Finish packet is used to tell the server that there is no more data and that
  it can close the established connection.
  FIN-ACK- [F.]: The Finish Acknowledgement packet is used to acknowledge that the previous
  Finish packet was received.
  RST- [R]: The Reset packet is used when the source system wishes to Reset the connection. In
  general, this is due to an error or the target port is not actually in the listening status.
  RST-ACK -[R.]: The Reset Acknowledgement packet is used to acknowledge that the previous
  Reset packet was received.
 
Now that we have explored the different types of packets, let's tie it all together and take a quick look
back at the data captured earlier.
[blog]# tcpdump -nvvv -r /var/tmp/chapter5.pcap host 192.168.33.12
reading from file /var/tmp/chapter5.pcap, link-type EN10MB (Ethernet)
www.hellodigi.ir
---------------
#################
Since the tcpdump captured a large number of packets, we will once again use the host filter to limit
results to the network traffic to and from 192.168.33.11.
[db]# tcpdump -nnvvv -r /var/tmp/alltraffic.pcap host 192.168.33.11
reading from file /var/tmp/alltraffic.pcap, link-type LINUX_SLL (Linux cooked)
15:37:51.616621 IP (tos 0x0, ttl 64, id 8389, offset 0, flags [DF], proto TCP 
(6), length 60)
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [S], cksum 0x34dd (correct), 
seq 4225047048, win 14600, options [mss 1460,sackOK,TS val 3357389 ecr 
0,nop,wscale 6], length 0
15:37:51.616665 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), 
length 60)
    192.168.33.12.3306 > 192.168.33.11.47339: Flags [S.], cksum 0xc396 
(incorrect -> 0x3609), seq 1637731271, ack 4225047049, win 14480, options [mss 
1460,sackOK,TS val 3330467 ecr 3357389,nop,wscale 6], length 0
15:37:51.616891 IP (tos 0x0, ttl 255, id 2947, offset 0, flags [none], proto TCP 
(6), length 40)
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [R], cksum 0x10c4 (correct), 
seq 4225047049, win 0, length 0
15:37:52.619386 IP (tos 0x0, ttl 64, id 8390, offset 0, flags [DF], proto TCP 
(6), length 60)
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [S], cksum 0x30f2 (correct), 
seq 4225047048, win 14600, options [mss 1460,sackOK,TS val 3358392 ecr 
0,nop,wscale 6], length 0
15:37:52.619428 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), 
length 60)
    192.168.33.12.3306 > 192.168.33.11.47339: Flags [S.], cksum 0xc396 
(incorrect -> 0x1987), seq 1653399428, ack 4225047049, win 14480, options [mss 
1460,sackOK,TS val 3331470 ecr 3358392,nop,wscale 6], length 0
15:37:52.619600 IP (tos 0x0, ttl 255, id 2948, offset 0, flags [none], proto TCP 
www.hellodigi.ir
---------------------Page 218---------------------
 
(6), length 40)
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [R], cksum 0x10c4 (correct), 
seq 4225047049, win 0, length 0
 
With the captured data, it seems that we have found the expected SYN-ACK. To show this in a clearer
fashion, let's trim the output to just the IPs and flags in use.
15:37:51.616621 IP
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [S],
15:37:51.616665 IP
    192.168.33.12.3306 > 192.168.33.11.47339: Flags [S.],
15:37:51.616891 IP
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [R],
15:37:52.619386 IP
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [S],
15:37:52.619428 IP
    192.168.33.12.3306 > 192.168.33.11.47339: Flags [S.],
15:37:52.619600 IP
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [R],
 
With a clearer picture, we can see an interesting series of network packets being transmitted.
15:37:51.616621 IP
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [S],
 
The first packet is an SYN packet from 192.168.33.11 to 192.168.33.12 on port 3306. This is the
same type of packet that we have captured with the earlier tcpdump executions.
15:37:51.616665 IP
    192.168.33.12.3306 > 192.168.33.11.47339: Flags [S.],
 
However, we have not seen the second packet before. In the second packet, we see that it is an SYN-
ACK (identified by Flags [S.]). The SYN-ACK is being sent from 192.168.33.12 on port 3306 to
192.168.33.11 on port 47339 (the port that sent the original SYN packet).
 
At the first glance, this seems to be a normal SYN and SYN-ACK handshake.
15:37:51.616891 IP
    192.168.33.11.47339 > 192.168.33.12.3306: Flags [R],
 
The third packet, however, is interesting as it is a clear indication of an issue. The third packet is a
RESET packet (identified by Flags [R]) sent from 192.168.33.11, the blog server. The interesting
thing about this is that, when executing tcpdump on the blog server, we never captured a RESET
packet. If we execute tcpdump again on the blog server, we can see this one more time.
[blog]# tcpdump -i any port 3306
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 65535 bytes
15:24:25.646731 IP blog.example.com.47336 > db.example.com.mysql: Flags [S], seq 
3286710391, win 14600, options [mss 1460,sackOK,TS val 2551514 ecr 0,nop,wscale 
www.hellodigi.ir
---------------------Page 219---------------------
 
6], length 0
15:24:26.648706 IP blog.example.com.47336 > db.example.com.mysql: Flags [S], seq 
3286710391, win 14600, options [mss 1460,sackOK,TS val 2552516 ecr 0,nop,wscale 
6], length 0
15:24:28.652763 IP blog.example.com.47336 > db.example.com.mysql: Flags [S], seq 
3286710391, win 14600, options [mss 1460,sackOK,TS val 2554520 ecr 0,nop,wscale 
6], length 0
15:24:32.660123 IP blog.example.com.47336 > db.example.com.mysql: Flags [S], seq 
3286710391, win 14600, options [mss 1460,sackOK,TS val 2558528 ecr 0,nop,wscale 
6], length 0
15:24:40.676112 IP blog.example.com.47336 > db.example.com.mysql: Flags [S], seq 
3286710391, win 14600, options [mss 1460,sackOK,TS val 2566544 ecr 0,nop,wscale 
6], length 0
15:24:56.724102 IP blog.example.com.47336 > db.example.com.mysql: Flags [S], seq 
3286710391, win 14600, options [mss 1460,sackOK,TS val 2582592 ecr 0,nop,wscale 
6], length 0
 
From the preceding tcpdump output, we never see either the SYN-ACK or the RESET packets on the
blog server. This either means that the RESET is being sent by another system or the SYN-ACK packet is
being rejected by the blog server's kernel before tcpdump can capture it.
 
When the tcpdump command captures network traffic, it does so after the kernel has processed this
network traffic. This means that if, for any reason, the kernel is rejecting the packet, it will not be
seen via the tcpdump command. Thus, it is possible that the blog server's kernel is rejecting the return
packets from the database server before tcpdump is able to capture them.
 
###############
root@linuxserver ~]# cat port80.txt | egrep -e "lhr35.*http.>.linuxserver.48244" | head
17:46:08.982413 IP lhr35s01-in-f14.1e100.net.http > linuxserver.48244: Flags [S.], seq 2120554953, ack 2658526350, win 64240, options [mss 1460], length 0
17:46:08.988543 IP lhr35s01-in-f14.1e100.net.http > linuxserver.48244: Flags [.], ack 430, win 64240, length 0

[root@linuxserver ~]# cat port80.txt | egrep -e "linuxserver.48244.>.lhr35" | head
17:46:08.848055 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [S], seq 2658526349, win 29200, options [mss 1460,sackOK,TS val 46470178 ecr 0,nop,wscale 7], length 0
17:46:08.982969 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [.], ack 1, win 29200, length 0
17:46:08.986088 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [P.], seq 1:430, ack 1, win 29200, length 429
17:46:09.156646 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [.], ack 747, win 30586, length 0

[root@linuxserver ~]# cat port80.txt | egrep -e "linuxserver.48244.>.lhr35" | egrep -e "seq.[0-9:0.9]"
17:46:08.848055 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [S], seq 2658526349, win 29200, options [mss 1460,sackOK,TS val 46470178 ecr 0,nop,wscale 7], length 0
17:46:08.986088 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [P.], seq 1:430, ack 1, win 29200, length 429
17:46:35.134568 IP linuxserver.48244 > lhr35s01-in-f14.1e100.net.http: Flags [P.], seq 430:859, ack 747, win 30586, length 429

[root@linuxserver ~]# cat port80.txt | egrep -e "lhr35.*http.>.linuxserver.48244" | egrep -e "seq.[0-9:0.9]"
17:46:08.982413 IP lhr35s01-in-f14.1e100.net.http > linuxserver.48244: Flags [S.], seq 2120554953, ack 2658526350, win 64240, options [mss 1460], length 0
17:46:09.156546 IP lhr35s01-in-f14.1e100.net.http > linuxserver.48244: Flags [P.], seq 1:747, ack 430, win 64240, length 746
17:46:35.673939 IP lhr35s01-in-f14.1e100.net.http > linuxserver.48244: Flags [P.], seq 747:1493, ack 859, win 64240, length 746

[root@linuxserver ~]# cat port80.txt | egrep -e "linuxserver.*.>." | egrep -e "seq.[0-9:0.9]" | head
17:41:47.702489 IP linuxserver.44178 > lhr25s10-in-f14.1e100.net.http: Flags [S], seq 342324833, win 29200, options [mss 1460,sackOK,TS val 46209032 ecr 0,nop,wscale 7], length 0
17:41:47.703653 IP linuxserver.44180 > lhr25s10-in-f14.1e100.net.http: Flags [S], seq 373984999, win 29200, options [mss 1460,sackOK,TS val 46209033 ecr 0,nop,wscale 7], length 0

####################
How is this possible? A Mandrill bug? Or maybe we have our message format wrong. Maybe weâ€™re using cURL wrong. So many possible theories, but we still didnâ€™t have enough data. We booted up my favorite tool, tcpdump. First, we checked the small message that worked:
 
23:26:12 IP ip-172.us-west-2.compute.internal.49493 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [S], length 0  // SYN
23:26:12 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.49493: Flags [S.], length 0 // SYN+ACK
23:26:12 IP ip-172.us-west-2.compute.internal.49493 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [.], length 0  // ACK
23:26:12 IP ip-172.us-west-2.compute.internal.49493 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [P.], length 212 // Data
23:26:12 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.49493: Flags [.], length 0  // ACK Data
23:26:12 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.49493: Flags [P.], length 390 // Data2
//..
23:27:12 IP ip-172.us-west-2.compute.internal.49493 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [FP.], length 37 // FIN
23:27:12 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.49493: Flags [R], length 0  // Connection closed
 
Everything looks fine. Connection opened and acknowledged. Data is sent after the TLS setup and then acknowledged just like youâ€™d expect.
 
We then sent the larger message to Mandrill and observed its results:
 
23:32:05 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [S], length 0  // SYN
23:32:05 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.58542: Flags [S.], length 0 // SYN+ACK
23:32:05 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [.], length 0  // ACK
23:32:06 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [P.], length 212 // Data
23:32:06 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.58542: Flags [.], length 0  // ACK Data
23:32:06 IP ec2-54.us-west-2.compute.amazonaws.com.https > ip-172.us-west-2.compute.internal.58542: Flags [P.], length 390 // Data2
//..
23:32:06 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [P.], length 1707 // Data3
23:32:06 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [P.], length 1707 // Data3 retransmit
23:32:07 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [P.], length 1707 // Data3 retransmit
23:32:07 IP ip-172.us-west-2.compute.internal.58542 > ec2-54.us-west-2.compute.amazonaws.com.https: Flags [P.], length 1707 // Data3 retransmit


