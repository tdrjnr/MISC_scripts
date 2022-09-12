import sys, os
from pprint import pprint
import operator
import argparse

def CheckLargeFiles(args):
	allsizes = []
	for (thisDir, subsHere, filesHere) in os.walk(args.dir):
		for filename in filesHere:
			filepath = os.path.join(thisDir, filename)
			filesize = os.path.getsize(filepath)
			allsizes.append((filesize, filepath))

	#pprint (allsizes)
	#allsizes.sort()
	allsizes.sort(key=operator.itemgetter(0))
	allsizesdict=dict((y, x) for x, y in allsizes)
	#print('Small', (allsizes[:3]))
	print('Large', allsizes[-3:])
	#pprint('Large', allsizes[-3:])
	#print (larg[1])
	#for i in larg:
		#print(type(i[0][0]))

if __name__ == "__main__":
	LargeFiles = argparse.ArgumentParser(prog='CheckLargeFiles',description='Find large files')
#IntExt = subparsers.add_parser('PtfRef', help='Ptf Table Ref')
LargeFiles.add_argument("-d", "--dir", required=True, help="Directory e.g. CheckLargeFiles.py -d /var/log")
LargeFiles.set_defaults(func=CheckLargeFiles)

args = LargeFiles.parse_args()
args.func(args)