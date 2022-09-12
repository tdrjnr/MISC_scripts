#!/usr/bin/bash

# A remake of https://gist.github.com/pavel-odintsov/9b065f96900da40c5301

if [ -z "$1" ]; then
    echo
    echo usage: $0 [network-interface]
    echo
    echo e.g. $0 eth0
    echo
    echo adjusts irg balance for NIC queues
    exit
fi
dev="$1"


ncpus=`nproc`
test "$ncpus" -gt 1 || exit 1
echo "CPUs: $ncpus"


echo "Existing irq affinity for $dev:"
for irq in `awk -F "[ :]" "/$dev/"'{print $2}' /proc/interrupts`
do
    awk "/$irq:/"'{printf "%s ", $NF}' /proc/interrupts
    cat /proc/irq/$irq/smp_affinity
done