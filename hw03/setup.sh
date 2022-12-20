#!/bin/bash

# !!! Installs dependencies for the homework
#pip3 install smbus

# !!! Set the pins for the rotary encoders

config-pin P8_33 eqep
config-pin P8_35 eqep    # This is really P9_41b

# eQEP 2		Warning, only configure one pair as a time.
#					If you do both as the same time the encoder won't work.
config-pin P8_11 eqep    # These have a conflict on the Green Wireless
config-pin P8_12 eqep

# !!! setup stuff for alerts
#i2cset -y 2 0x49 1 0x60
#i2cset -y 2 0x4a 1 0x60
