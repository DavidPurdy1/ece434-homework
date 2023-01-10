#!/bin/bash

# This script reads the i2c data from the kernel driver for the tmp101 sensors

ADDR1=0x49
ADDR2=0x4a

# "Ignore resource busy errors, this is expected if the temp sensors are already loaded"
echo "Warning.. Might fail on the first time due to initializing. Rerun again."
echo ""

# echo "Telling kernel driver to read from tmp101 sensor at address $ADDR1..."
echo tmp101 $ADDR1 > /sys/class/i2c-adapter/i2c-2/new_device >> /dev/null

# echo "Telling kernel driver to read from tmp101 sensor at address $ADDR2..."
echo tmp101 $ADDR2 > /sys/class/i2c-adapter/i2c-2/new_device >> /dev/null

TEMP1=`cat /sys/bus/i2c/devices/2-0049/hwmon/hwmon0/temp1_input`
TEMP2=`cat /sys/bus/i2c/devices/2-004a/hwmon/hwmon1/temp1_input`

echo "Temp 1 $(($TEMP1 / 1000)) degrees C"
echo "Temp 2 $(($TEMP2 / 1000)) degrees C"