#!/usr/bin/env python3
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
from flask import Flask, render_template, request
from adxl345 import ADXL345
app = Flask(__name__)

# HW05 - Etch-a-Sketch
# David Purdy 1-26-2023

# set up the LED matrix i2c stuff
bus = smbus.SMBus(2)
matrix_address = 0x70
# set up the LED matrix
bus.write_byte_data(matrix_address, 0x21, 0)
bus.write_byte_data(matrix_address, 0x81, 0)
bus.write_byte_data(matrix_address, 0xe7, 0)

xMax = 8
yMax = 8
x = 0
y = 0

adxl345 = ADXL345()

# check that arguments are integers, else throw error
grid = [['.' for i in range(xMax)] for j in range(yMax)]

def print_grid(g):
  printarr = []
  printarr.append([i for i in range(xMax)])
  printarr[0].insert(0," ")
  for row in g:
    printarr.append(row)
  for i in range(len(printarr) - 1):
    printarr[i + 1].insert(0,i)
    
  mx = len(str(xMax)) # get max amount of digits in x
  for row in printarr:
    print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
  print()

  for row in g:
    row.pop(0)

# the led matrix is accessable by column, not row
# so check if each row in a column is a star, if so, it is a 1 in the binary string
def led_matrix_update(grid):
    matrix_grid = ["", "", "", "", "", "", "", ""]
    # for along columns in grid, create binary string
    for i in range(len(grid)):
      for j in range(len(grid)):
        if grid[j][i] == '*':
          matrix_grid[i] += '1'
        else:
          matrix_grid[i] += '0'

    # convert binary strings to integers
    for i in range(len(matrix_grid)):
      matrix_grid[i] = int(matrix_grid[i], 2)

    # make them only the red for now
    i2c_block_data = []
    for i in range(len(matrix_grid)):
      i2c_block_data.append(0)
      i2c_block_data.append(matrix_grid[i])
    # write to the i2c bus
    bus.write_i2c_block_data(matrix_address, 0, i2c_block_data)

def print_welcome():
  print("Welcome to the etch-a-sketch simulator!")
  print("Commands:")
  print("  u - move up")
  print("  d - move down")
  print("  l - move left")
  print("  r - move right")
  print("  c - clear the screen")
  print("  q - quit")
  print()

grid[y % yMax][x % xMax] = '*'
print_grid(grid)
led_matrix_update(grid)


while True:

  # get accelerometer data
  axes = adxl345.getAxes(True)
  axesy = axes['y']
  axesx = axes['x']
  print(axesy)
  print(axesx)

  # if the accelerometer is tilted more than 1.5g in any direction
  if axesy < -0.1:
    y-=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)

  if axesy > 0.1:
    y+=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)

  if axesx > 0.1:
    x-=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)

  if axesx < -0.1:
    x+=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)
