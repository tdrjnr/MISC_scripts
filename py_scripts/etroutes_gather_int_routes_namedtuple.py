#!/usr/bin/python2.7
#####!/usr/local/anaconda/bin/python2.7 # f6

import os, sys
import platform
sys.path.append("/mnt/storage/python2.7.modules") # laptop

import glob,glob2
from collections import namedtuple

from tabulate import tabulate
from prettytable import PrettyTable
import argparse
#hostname = 'vm-se1'



hostname = platform.uname()[1]


#path = ('/home/f645523/sh_scripts/network') # f6
path = ('/mnt/storage/scripts/shell/network') #laptop

files = glob2.glob(path+'/**/*.*', recursive=True)

netroutes = []
netroutes1 = []

for filename in files:
	if filename.__contains__('netstat'):
	#if filename.__contains__('ethtool'):
	#if filename.__contains__('wlp3'):
	#if filename.find('netstat'):
	#if filename.endswith("'") or filename.endswith('"'):
		#print filename
		with open(filename, 'rb') as f:
			for line in f:
				#print line
				if line.startswith('Destination') or line.startswith('Kernel'):
					continue
				else:
					#print line
					netroutes.append(line)


introutes = {}
hostroutes = {}

netroutes = map(lambda x: str.replace(x, "\n", ""), netroutes)

for x in netroutes:
	x = x.split()
	netroutes1.append(x)


#hostname='vmse1'
#hostname1 = 'vm-se1'

hostroutes[hostname] = introutes

###################################

#Row = namedtuple(hostname,["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"])
Node = namedtuple(hostname,["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"])
#int_routes_namedtuple = Row(*netroutes1[0])

list_int_routes_namedtuple = []

for x in netroutes1:
	#print Row(*x)
	#list_int_routes_namedtuple.append(Row(*x))
	list_int_routes_namedtuple.append(Node(*x))

#print list_int_routes_namedtuple

print " "
print "Hostname",   "Iface",   "Gateway",   "Destination"
for i in list_int_routes_namedtuple.__iter__():
	#print hostname+' '+ i.Iface, i.Gateway, i.Destination
	print hostname+' '+ i.Iface, i.Gateway, i.Destination
	#print tabulate(hostname,i.Iface,i.Gateway,i.Destination, headers=["Hostname","Iface","Gateway","Destination"])

'''
Row = namedtuple(hostname,["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"])
#int_routes_namedtuple = Row(*netroutes1[0])

list_int_routes_namedtuple = []

for x in netroutes1:
	#print Row(*x)
	list_int_routes_namedtuple.append(Row(*x))
'''
