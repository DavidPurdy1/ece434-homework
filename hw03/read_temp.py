#!/usr/bin/env python3

# read_temp.py
# reads the temperature from the TMP101 sensor
# Author: David Purdy

# !!! import the smbus library with pip
import smbus

TMP101_ADDR = 0x49
TMP101_ADDR_2 = 0x4a
bus = smbus.SMBus(2)


temp = bus.read_byte_data(TMP101_ADDR, 0)
temp2 = bus.read_byte_data(TMP101_ADDR_2, 0)
print("Temp 1 sensor is %d Celcius" %(temp))
print("Temp 1 sensor is %d Farenheit" %(temp * 9/5 + 32))
print("Temp 2 sensor is %d Celcius" %(temp2))
print("Temp 2 sensor is %d Farenheit" %(temp2 * 9/5 + 32))