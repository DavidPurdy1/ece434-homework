#!/bin/bash

# Reads temperature from TMP101 sensor connected to I2C bus
# Author: David Purdy

# Make sure that tmp101 addresses are correct or else script fails
temp=`i2cget -y 2 0x49`
celcius=$(($temp | bc))
farenheit=$(($temp * 9/5 + 32))

temp2=`i2cget -y 2 0x4a`
celcius2=$(($temp2 | bc))
farenheit2=$(($temp2 * 9/5 + 32))

echo "Temperature is $celcius degrees C for sensor 1"
echo "Temperature is $farenheit degrees F for sensor 1"
echo " "
echo "Temperature is $celcius2 degrees C for sensor 2"
echo "Temperature is $farenheit2 degrees F for sensor 2"
