#!/usr/bin/python2.7

import os
import re
import sys
import time

#sys.path.append('/usr/local/anaconda/lib') #f6
#sys.path.append('/usr/local/anaconda/lib/python2.7/site-packages') # f6

sys.path.append('/mnt/storage/python2.7.modules') # laptop

import glob
import glob2

from tabulate import tabulate
from prettytable import PrettyTable



files = glob2.glob('/proc/irq/*/smp_*', recursive=True)

dirs = os.listdir('/proc/irq/')
smpirq = [dir for dir in dirs if dir.isdigit()]


def build_up_list(filename_pattern, list_of_files):
    result = []
    for filename in list_of_files:
        if filename.endswith(filename_pattern):
            with open(filename, 'rb') as f:
                filename=filename.split('/')
                for line in f:
                    result.append(line.strip())
    return result

smpmask = build_up_list('smp_affinity', files)
smplist = build_up_list('smp_affinity_list', files)
          
smpirqmask=dict(zip(smpirq, zip(smpmask, smplist)))


f_interrupts = open("/proc/interrupts", "r")
f_interrupts.seek(0)
#ts = int(time.time())
irqtab=[]
num_cpus = len(f_interrupts.readline().split())
for line in f_interrupts:
    cols = line.split()
    #print cols
    if len(cols) == 2:
        continue
    #print cols

    irq_type = cols[0].rstrip(":")
    irq_type2=cols[3]+' '+cols[4]
    #irq_type2=cols[4]
    for i, val in enumerate(cols[1:]):
        #irqtab=[]
        if i >= num_cpus:
            break
        if not val.isdigit():
            #there should only be digit values
            sys.stderr.write("Unexpected interrupts value %r in"
                             " %r: " % (val, cols))
            break
        if irq_type.isdigit():
            print ("proc.interrupts=%s | type=%s | desc=%s | CPU=%s | Mask=%s | Aff=%s" % (val, irq_type, irq_type2, i, smpirqmask[irq_type][0],smpirqmask[irq_type][1]))
            #print tabulate(val, irq_type, irq_type2, i, smpirqmask[irq_type][0],smpirqmask[irq_type][1], headers=["Interrupts","Type","Desc","CPU","Mask","Aff"])


