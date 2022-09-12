#!/usr/bin/bash
#set -x
# from http://habrahabr.ru/post/108240/
#ncpus=`grep -ciw ^processor /proc/cpuinfo`

for irq in `cat /proc/interrupts | awk '{print $1}' | sed s/\://g`
#for irq in `cat /proc/interrupts | awk '{print $1}' | sed s/\://g | egrep -e [0-9]`
do
    #f="/proc/irq/$irq/smp_affinity"
    #echo "/proc/irq/$irq/smp_affinity/"
    echo `cat /proc/irq/$irq/smp_affinity`
    #echo `grep . -R /proc/irq/$irq/smp_affinity`

done
#/proc/irq/0/smp_affinity/
#/proc/irq/1/smp_affinity/
#/proc/irq/8/smp_affinity/