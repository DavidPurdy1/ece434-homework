#!/usr/bin/env python3

# when temp is above a certain limit, interrupt is given from the TMP101 and alerts something
import smbus
import Adafruit_BBIO.GPIO as GPIO
import time

# set up gpio pins
GPIO.setup("P8_16", GPIO.IN)
GPIO.setup("P8_18", GPIO.IN)
GPIO.cleanup()

bus = smbus.SMBus(2)

Thigh = 23
Tlow = 19

T1 = 0x49
T2 = 0x4a
# set up the TMP101 1
bus.write_byte_data(T1, 1, 0x60)
bus.write_byte_data(T1, 2, Thigh)
bus.write_byte_data(T1, 3, Tlow)

# set up the TMP101 2
bus.write_byte_data(T2, 1, 0x60)
bus.write_byte_data(T2, 2, Thigh)
bus.write_byte_data(T2, 3, Tlow)

# wait for an interrupt on the alert pin, if so print the temp
oldata = -1
oldata2 = -1
while True:
  # check if pin is set
    if GPIO.input("P8_16") == 0:
      data = bus.read_i2c_block_data(T1, 0, 2)
      data = data[0]
      if data != oldata:
        print("Temp 1 in degrees celcius: ", data)
        print("Temp 1 in degrees farenheit: ", round(data * 1.8 + 32))
      oldata = data
    if GPIO.input("P8_18") == 0:
      data2 = bus.read_i2c_block_data(T2, 0, 2)
      data2 = data2[0]
      if data2 != oldata2:
        print("Temp 2 in degrees celcius: ", data2)
        print("Temp 2 in degrees farenheit: ", round(data2 * 1.8 + 32))
      oldata2 = data2
    time.sleep(.1)
