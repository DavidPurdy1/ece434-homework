#!/usr/bin/env python
# Toggle GPIO pin as fast as possible

import Adafruit_BBIO.GPIO as GPIO
import time
import sys

# get commandline arguments
if len(sys.argv) != 2:
    print("Usage: python toggle_gpio_fast.py <delay>")
    sys.exit(1)

try:
  delay = float(sys.argv[1])
except ValueError:
  print("Usage: ./program delay")
  print("delay must be an number")
  sys.exit(1)

# convert commandline argument to int and if fail exit 

# Set up GPIO pin
GPIO.setup("P8_11", GPIO.OUT)

# Toggle GPIO pin as fast as possible
while True:
    GPIO.output("P8_11", GPIO.HIGH)
    time.sleep(delay)
    GPIO.output("P8_11", GPIO.LOW)
