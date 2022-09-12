#!/usr/bin/python2.7
#####!/usr/local/anaconda/bin/python2.7 # f6
import os
import sys
import platform
sys.path.append("/mnt/storage/python2.7.modules") # laptop
import glob,glob2

from tabulate import tabulate
from prettytable import PrettyTable
import pprint as pp


#hostname = 'vm-se1'
hostname = platform.uname()[1]

netroutes = []
introutes = {}

hostroutes = {}


#path = ('/home/f645523/sh_scripts/network') # f6
path = ('/mnt/storage/scripts/shell/network') #laptop
files = glob2.glob(path+'/**/*.*', recursive=True)

#netroutes_header = ["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"]
#netroutes_header = ["Destination","Gateway","Iface"]

#netroutes = map(lambda x: str.replace(x, "\n", ""), netroutes)

def GetRoutes(file):
	for filename in files:
		if filename.__contains__('netstat'):
			with open(filename, 'rb') as f:
				for line in f:
					if line.startswith('Destination') or line.startswith('Kernel'):
						continue
					else:
						netroutes.append(line)
	return netroutes

netroutes = GetRoutes(files)
netroutes = map(lambda x: str.replace(x, "\n", ""), netroutes)



for x in netroutes:
	x = x.split()
	destination = x[0]
	gateway = x[1]
	iface = x[7]
	introutes[iface] = gateway,destination

hostroutes[hostname] = introutes
#print (hostroutes)
#pp.pprint(hostroutes)
print tabulate(list(hostroutes.items()),headers=["Server","   Int       Gateway     Dest"])
#print tabulate(list(hostroutes.items()),headers=["Server","   Int     Gateway   Dest","Def"], tablefmt='html')


#print tabulate(hostroutes.keys(),hostroutes.values
#print tabulate(val, irq_type, irq_type2, i, smpirqmask[irq_type][0],smpirqmask[irq_type][1], headers=["Interrupts","Type","Desc","CPU","Mask","Aff"]))

#print "{:<8} {:<15} {:<10}".format('Key','Label','Number')
#for k, v in d.iteritems():
 #   label, num = v
  #  print "{:<8} {:<15} {:<10}".format(k, label, num)





"""
In [14]: !netstat -rn
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.0.1     0.0.0.0         UG        0 0          0 wlp3s0
192.168.0.0     0.0.0.0         255.255.255.0   U         0 0          0 wlp3s0
192.168.122.0   0.0.0.0         255.255.255.0   U         0 0          0 virbr0

In [12]: introutes
Out[12]: {'virbr0': ('0.0.0.0', '192.168.122.0'), 'wlp3s0': ('0.0.0.0', '192.168.0.0')}


  In [9]: hostroutes['linuxserver']['virbr0'][0]
Out[9]: '0.0.0.0'

In [10]: hostroutes['linuxserver']['virbr0'][1]
Out[10]: '192.168.122.0'

In [41]: print tabulate(list(hostroutes.items()),headers=["Server","   Int       Gateway     Dest"])
Server          Int       Gateway     Dest
-----------  ------------------------------------------------------------------------------
linuxserver  {'wlp3s0': ('0.0.0.0', '192.168.0.0'), 'virbr0': ('0.0.0.0', '192.168.122.0')}

"""