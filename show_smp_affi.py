#!/bin/bash

function dump_irq_smp_affinity {

	irqlist=`grep $1 /proc/interrupts | awk -F: '{print $1}'`
	printf "\n"
	for irq in $irqlist
	do
		name=`get_vect_name $irq`
		value=`cat /proc/irq/$irq/smp_affinity`
		
		if [ -f /proc/irq/$irq/smp_affinity_list ]
		then
			cpu_list=`cat /proc/irq/$irq/smp_affinity_list`
			printf "%30s %40s CPU %s\n" $name $value $cpu_list
		else
			printf "%30s %40s\n" $name $value
		fi
	done;
}

echo "Current vector filter is "${vect_array[@]}""
echo "Interval is $INTERVAL, use CTRL+C to quit..."

while (true)
do
	for ((i=0;i<${#vect_array[@]};i++))
	do
		dump_irq_smp_affinity ${vect_array[$i]}
	done

	sleep $INTERVAL
done;
