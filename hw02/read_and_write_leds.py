#!/usr/bin/python

#
# Test read and write to GPIO pins
# author: David Purdy
#

import Adafruit_BBIO.GPIO as GPIO
import time

# set up gpio pins
GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)
GPIO.setup("P8_16", GPIO.OUT)
GPIO.setup("P8_18", GPIO.OUT)

GPIO.setup("P8_11", GPIO.IN)
GPIO.setup("P8_13", GPIO.IN)
GPIO.setup("P8_19", GPIO.IN)
GPIO.setup("P8_17", GPIO.IN)

GPIO.cleanup()


while True:
  if GPIO.input("P8_11") == 1:
    print("HIGH 11")
    GPIO.output("P8_12", GPIO.HIGH)

  if GPIO.input("P8_13") == 1:
    print("HIGH 13")
    GPIO.output("P8_14", GPIO.HIGH)

  if GPIO.input("P8_19") == 1:
    print("HIGH 19")
    GPIO.output("P8_16", GPIO.HIGH)

  if GPIO.input("P8_17") == 1:
    print("HIGH 17")
    GPIO.output("P8_18", GPIO.HIGH)

  time.sleep(0.5)

  GPIO.output("P8_12", GPIO.LOW)
  GPIO.output("P8_14", GPIO.LOW)
  GPIO.output("P8_16", GPIO.LOW)
  GPIO.output("P8_18", GPIO.LOW)