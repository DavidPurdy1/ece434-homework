#!/bin/bash

# Reads temperature from TMP101 sensor connected to I2C bus
# Author: David Purdy

temp=`i2cget -y 2 0x48`
farenheit=$(($temp * 9/5 + 32))

echo "Temperature is $farenheit degrees F"