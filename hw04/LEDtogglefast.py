#!/usr/bin/env python3
# From: https://graycat.io/tutorials/beaglebone-io-using-python-mmap/
from mmap import mmap
import time, struct

# Read 2 inputs and outputs to LEDs using mmap

# Mapping the entire /dev/mem file would require that over a gigabyte be
# allocated in Python's heap, so the offset address and size variables are 
# used to keep the mmap as small as possible, in this case just the GPIO1 register. 
# These values are straight out of the memory map in section 2.1 of the 
# Technical Reference Manual. the GPIO_OE, GPIO_SETDATAOUT and GPIO_CLEARDATAOUT 
# addresses are found in section 25.4, which shows the address offsets of each 
# register within the GPIO modules, starting from the base module address. 
# Chapter 25 explains how to use the GPIO registers. 
# All we need to do is set a pin as an output, then set and clear its output state. 
# To do the first, we need the 'output enable' register (GPIO_OE above). 
# Then the GPIO_SETDATAOUT and GPIO_CLEARDATAOUT registers will do the rest. 
# Each one of these registers is 32 bits long, each bit of which corresponding 
# to one of 32 GPIO pins, so for pin 24 we need bit 24, or 1 shifted left 24 places.

GPIO0_offset = 0x44e07000
GPIO1_offset = 0x4804c000

GPIO0_size = 0x44e07fff-GPIO0_offset
GPIO1_size = 0x4804cfff-GPIO1_offset

GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
GPIO_DATAIN = 0x138

LED1 = 1<<26
LED2 = 1<<23
SW1_LINE = 12
SW2_LINE = 13
SW1 = 1<<SW1_LINE
SW2 = 1<<SW2_LINE

# Next we need to make the mmap, using the desired size and offset:
with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO0_size, offset=GPIO0_offset)
  mem2 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

# The mmap is addressed byte by byte, so we can't just set a single bit. 
# The easiest thing to do is grab the whole 4-byte register:
output_packed_reg = mem[GPIO_OE:GPIO_OE+4]
input_packed_reg = mem2[GPIO_OE:GPIO_OE+4]

# We now have 32 bits packed into a string, so to do any sort of bitwise operations with it we must unpack it:
# The 'L' tells struct.unpack() to unpack the string into an unsigned long, 
# which will give us the full 32-bit register. The '<' tells it that the 
# string is packed little-endian, or least-significant byte first. 
# The BeagleBone's memory is little-endian, so if we tell this to struct.unpack() 
# it will return the 32 bits in the order they are shown in the reference manual register maps.
output_reg_status = struct.unpack("<L", output_packed_reg)[0]
input_reg_status = struct.unpack("<L", input_packed_reg)[0]

# We now have the 32-bit integenteger value of the register, so we can configure 
# the LED as an output by clearing value of the register, so we can configure 
# the LED as an output by clearing its bit:
output_reg_status &= ~(LED1)
output_reg_status &= ~(LED2)
# set the switch as an inputs
input_reg_status |= (SW1)
input_reg_status |= (SW2)

# Now all that's left to do is to pack it little-endian back into a string and update the mmap:

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", output_reg_status)
mem2[GPIO_OE:GPIO_OE+4] = struct.pack("<L", input_reg_status)

# Now that we know the pin is configured as an output, it's time to get blinking. 
# We could use the GPIO_DATAOUT register to do this, 
# but we would want to preserve the state of all the other bits in it, 
# so we would need to do the same process of unpacking, manipulating then repacking. 
# That's what the SETDATAOUT and CLEARDATAOUT registers are for. 
# Writes to them affect only the pins whose bits are set to 1, making the next step much easier:
try:
  while(True):
    # check if the button is pressed
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED1)
    time.sleep(0.05)
    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED1)
    time.sleep(0.05)

except KeyboardInterrupt:
  mem.close()