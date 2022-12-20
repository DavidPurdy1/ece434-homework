#!/usr/bin/env python3

# when temp is above a certain limit, interrupt is given from the TMP101 and alerts something
import smbus
import Adafruit_BBIO.GPIO as GPIO

# set up gpio pins
GPIO.setup("P8_16", GPIO.IN)
GPIO.setup("P8_18", GPIO.IN)

# wait for an interrupt on the alert pin, if so print the temp
while True:
    if GPIO.input("P8_16") == 1:
        print("Temp 1 is above limit")
    if GPIO.input("P8_18") == 1:
        print("Temp 2 is above limit")