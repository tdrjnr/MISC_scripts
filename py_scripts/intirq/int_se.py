#######!/usr/local/python2.7/bin/python2.7

import os
import re
import sys
import time
sys.path.append('/usr/local/anaconda/lib')
sys.path.append('/usr/local/anaconda/lib/python2.7/site-packages')
#sys.path.append("/mnt/storage/python2.7.modules") # laptop
import glob
import glob2

#sys.path.append('/mnt/storage/python2.7.modules')

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
# Get number of CPUs from description line.
num_cpus = len(f_interrupts.readline().split())
for line in f_interrupts:
    cols = line.split()
    #print cols
    if len(cols) == 2:
        continue
    #print cols

    irq_type = cols[0].rstrip(":")
    #irq_type2 =irq_type+' '+cols[6]
    #print irq_type
    #print irq_type+' '+cols[6]
    #print cols[5]+' '+cols[6]
    #irq_type2=cols[5]+' '+cols[6]
    irq_type2=cols[3]+' '+cols[4]
    #irq_type2=cols[4]
    for i, val in enumerate(cols[1:]):
        if i >= num_cpus:
            # All values read, remaining cols contain textual
            # description
            break
        if not val.isdigit():
            #there should only be digit values
            sys.stderr.write("Unexpected interrupts value %r in"
                             " %r: " % (val, cols))
            break
        #print ("proc.interrupts %s type=%s cpu=%s" % (val, irq_type, i))
        #print ("IntCount=%s IntType=%s CPU=%s" % (val, irq_type, i))
        #print irq_type2
        #print ("proc.interrupts=%s type=%s desc=%s CPU=%s" % (val, irq_type, irq_type2, i))
        if irq_type.isdigit():
            print ("proc.interrupts=%s | type=%s | desc=%s | CPU=%s | Mask=%s | Aff=%s" % (val, irq_type, irq_type2, i, smpirqmask[irq_type][0],smpirqmask[irq_type][1]))
        
