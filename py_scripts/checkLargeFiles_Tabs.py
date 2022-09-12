#! /usr/bin/python
import sys, os
sys.path.append('/mnt/storage/python2.7.modules')
from pprint import pprint
import operator
import argparse
from tabulate import tabulate
from prettytable import PrettyTable

def CheckLargeFiles(args):
	try:
		Folddir = []
		for (thisDir, subsHere, filesHere) in os.walk(args.dir, followlinks=False):
			for filename in filesHere:
				filepath = os.path.join(thisDir, filename)
				if os.path.islink(filepath):
					continue
				filesize = os.path.getsize(filepath)
				#filesize = os.stat(filepath).st_size
				Folddir.append((filesize, filepath))

		#pprint (Folddir)
		#Folddir.sort()
		Folddir.sort(key=operator.itemgetter(0))
		#Folddirdict=dict((y, x) for x, y in Folddir)
		#print('Small', (Folddir[:3]))
		#print('Large', Folddir[-3:])
		#print(Folddir)
		Folddir10=Folddir[-10:]
		#pprint('Large', Folddir[-3:])
		#print (larg[1])
		#print (Folddir10)
		result = (a[0]/1024/1024 for a in Folddir10)
		print tabulate(zip(Folddir10, list(result)), headers=['Bytes          Files', 'Mb'])
		
		#print tabulate(zip(Folddir10, list(result)), headers=['Bytes          Files', 'Mb'],tablefmt='orgtbl')
		#print(list(result))
		#print(list(zip(Folddir10, list(result))))
		#for item in zip(Folddir10, list(result)):
			#print ('File {} is {} Bytes and {} Mbytes in size'.format(item[0][1], item[0][0], item[1]))
			#print ('{} | Bytes={} | Mb={}'.format(item[0][1], item[0][0], item[1]))
			#print ('{: >10} | {: >2} Bytes | {: >2}Mb'.format(item[0][1], item[0][0], item[1]))
			#print "%-*s Bytes: %-*s  Mb: %-*s" % (20,item[0][1], item[0][0], item[1])
			#print tabulate(item, headers=['Bytes', 'Files'])

		#for i in larg:
			#print(type(i[0][0]))
		return result
	except Exception as e:
	#except OSError:
		print('Failed: %s' %str(e))
		#print('Success')
		raise
	return

if __name__ == "__main__":
	LargeFiles = argparse.ArgumentParser(prog='CheckLargeFiles',description='Find large files')
LargeFiles.add_argument("-d", "--dir", required=True, help="Directory e.g. CheckLargeFiles.py -d /var/log")
LargeFiles.set_defaults(func=CheckLargeFiles)

args = LargeFiles.parse_args()
args.func(args)
