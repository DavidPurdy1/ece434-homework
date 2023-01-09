#!/usr/bin/env python3
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
from flask import Flask, render_template, request
app = Flask(__name__)

# HW04 - Etch-a-Sketch
# David Purdy 1-7-2023

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

@app.route("/")
def index():
	# Read Sensors Status
  ledRedSts = '0'
  templateData = { 'title': 'GPIO output Status!', 'ledRed': ledRedSts,}
  return render_template('index.html', **templateData)
	
@app.route("/<action>")
def action(action):
  global x
  global y
  global grid
  global xMax
  global yMax

  if action == "up":
    y-=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)
  if action == "down":
    y+=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)
  if action == "left":
    x-=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)
  if action == "right":
    x+=1
    grid[y % yMax][x % xMax] = '*'
    led_matrix_update(grid)
    print_grid(grid)
    time.sleep(0.2)
  if action == "clear":
    y = 0
    x = 0
    grid = [['.' for i in range(xMax)] for j in range(yMax)]
    grid[y % yMax][x % xMax] = '*'

    print_grid(grid)
    led_matrix_update(grid)
    time.sleep(0.2)

		     
  templateData = { 'action': action, }

  return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)