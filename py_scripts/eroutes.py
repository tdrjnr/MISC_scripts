import os, sys
import glob,glob2
from collections import namedtuple


#files = glob2.glob(path+"/*net*") # netstat files
#glob2.glob("**/*") #all files - two directories down
	
#glob2.glob("**/**")
#files = glob2.glob("**/*")

#len(glob2.glob(path+"/**/*"))
#files = glob2.glob(path+"/**/*")
hostname = 'vm-se1'

path = ('X:\\clypcal\\JPM\\scripts\\WORKING\\scripts\\shell\\network')
files = glob2.glob(path+'/**/*.*', recursive=True)

'''
for filename in files:
	with open(filename, 'rb') as f:
		for line in f:
			print line
'''
netroutes = []
netroutes1 = []
#netroutes_header = ["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"]
#netroutes_header = ["Destination","Gateway","Iface"]
#netroutes.append(netroutes_header)


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

#print (len(netroutes))
#net_routes = tlist[2:]

#net_routes = tlist1=(tlist[2:])

#tuple(tlist[:])
#net_routes = tuple(tlist[2:])

#netroutes[0].split()


introutes = {}
hostroutes = {}

netroutes = map(lambda x: str.replace(x, "\n", ""), netroutes)

for x in netroutes:
	x = x.split()
	#print i
	#x = x[7]
	#print x
	#destination = x[0]
	#gateway = x[1]
	#iface = x[7]
	#introutes[iface] = gateway,destination
	netroutes1.append(x)
	#print x[7]


hostname='vmse1'
hostroutes[hostname] = introutes

################################### convert dictionary to a namedtuple
def convert(dictionary):
    return namedtuple('GenericDict', dictionary.keys())(**dictionary)

int_routes_namedtuple = convert(introutes)

#################################### append list with namedtuple contents
Row = namedtuple("Row",["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"])
#int_routes_namedtuple = Row(*netroutes1[0])

list_int_routes_namedtuple = []

for x in netroutes1:
	#print Row(*x)
	list_int_routes_namedtuple.append(Row(*x))
	
####################################
Row2 = namedtuple('interface', ['gateway', 'destination'])
Row2(*introutes)



>>> from collections import namedtuple
>>> Row = namedtuple('Row', ['first', 'second', 'third'])
>>> A = ['1', '2', '3']
>>> Row(*A)
Row(first='1', second='2', third='3')

'''
from collections import namedtuple
def convert(dictionary):
    return namedtuple('GenericDict', dictionary.keys())(**dictionary)
'''

'''

In [82]: %paste
def convert(dictionary):
    return namedtuple('GenericDict', dictionary.keys())(**dictionary)

## -- End pasted text --

In [83]: introutes
Out[83]: {'virbr0': ('0.0.0.0', '192.168.122.0'), 'wlp3s0': ('0.0.0.0', '192.168.0.0')}

In [84]: convert(introutes)
Out[84]: GenericDict(wlp3s0=('0.0.0.0', '192.168.0.0'), virbr0=('0.0.0.0', '192.168.122.0'))

In [85]: sd=convert(introutes)

In [86]: sd
Out[86]: GenericDict(wlp3s0=('0.0.0.0', '192.168.0.0'), virbr0=('0.0.0.0', '192.168.122.0'))

In [87]: sd.
sd.count  sd.index  sd.virbr0 sd.wlp3s0

In [87]: sd.virbr0
Out[87]: ('0.0.0.0', '192.168.122.0')
'''
>>> from collections import namedtuple
>>> Row = namedtuple('Row', ['first', 'second', 'third'])
>>> A = ['1', '2', '3']
>>> Row(*A)
Row(first='1', second='2', third='3')


'''
#from collections import namedtuple
###Vision = namedtuple('Vision', ['left', 'right'])
##Vision = namedtuple('Vision', ['interface', 'gateway', 'destination'])
#vision = Vision(introutes.keys, introutes.values()[0][0],introutes.values()[0][1])
'''

fields = ["Destination","Gateway","Genmask","Flags","MSS","Window","irtt","Iface"]
Town = collections.namedtuple('Town', fields)
funkytown = Town('funky', 300, 'somewhere', 'lipps', 'chicken')




'''
fields = ['name', 'population', 'coordinates', 'capital', 'state_bird']
>>> Town = collections.namedtuple('Town', fields)
>>> funkytown = Town('funky', 300, 'somewhere', 'lipps', 'chicken')
>>> funkytown._asdict()


OrderedDict([('name', 'funky'),
             ('population', 300),
             ('coordinates', 'somewhere'),
             ('capital', 'lipps'),
             ('state_bird', 'chicken')]
>>> Town = collections.namedtuple('Town', fields)
>>> funkytown = Town('funky', 300, 'somewhere', 'lipps', 'chicken')
>>> funkytown._asdict()
OrderedDict([('name', 'funky'),
             ('population', 300),
             ('coordinates', 'somewhere'),
             ('capital', 'lipps'),
             ('state_bird', 'chicken')]
'''