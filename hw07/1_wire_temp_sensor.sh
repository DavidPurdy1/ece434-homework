#!/bin/bash

T1=`cat /sys/class/hwmon/hwmon0/temp1_input`
T2=`cat /sys/class/hwmon/hwmon1/temp1_input`
T3=`cat /sys/class/hwmon/hwmon2/temp1_input`

T1_C=$(($T1/1000))
T2_C=$(($T2/1000))
T3_C=$(($T3/1000))

echo "Temperature 1: $T1_C C"
echo "Temperature 2: $T2_C C"
echo "Temperature 3: $T3_C C"
