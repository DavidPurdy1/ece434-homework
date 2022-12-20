#!/usr/bin/env python3
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

# HW03 - Etch-a-Sketch
# David Purdy 12-13-2022

# Gpio pins for the buttons
GPIO.setup("P8_13", GPIO.IN)
GPIO.setup("P8_14", GPIO.IN)
GPIO.setup("P8_15", GPIO.IN)
GPIO.setup("P8_17", GPIO.IN)
GPIO.cleanup()

# set up the LED matrix i2c stuff
bus = smbus.SMBus(2)
matrix_address = 0x70
# set up the LED matrix
bus.write_byte_data(matrix_address, 0x21, 0)
bus.write_byte_data(matrix_address, 0x81, 0)
bus.write_byte_data(matrix_address, 0xe7, 0)

# rotary encoders
left = '1'
right = '2'
ms = 100
maxCount = '1000000'

def init(eQep):
    counterpath = '/dev/bone/counter/'+eQep+'/count0'

    with open(counterpath+'/ceiling', 'w') as f:
        f.write(maxCount)
    
    with open(counterpath+'/enable', 'w') as f:
        f.write('1')

    return open(counterpath+'/count', 'r')


if len(sys.argv) != 3:
  print("Usage: etch-e-sketch.py gridXLength gridYLength")
  sys.exit(1)

xMax = 8
yMax = 8
x = 0
y = 0

# check that arguments are integers, else throw error
try:
  xMax = int(sys.argv[1])
  yMax = int(sys.argv[2])
except ValueError:
  print("Usage: etch-e-sketch.py xMax yMax")
  print("xMax and yMax must be integers")
  sys.exit(1)

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

f1 = init(left)
f2 = init(right)

# get initial values
f1.seek(0)
f2.seek(0)
olddata = int(f1.read()[:-1])
olddata2 = int(f2.read()[:-1])

# encoder loop

while True:
  f1.seek(0)
  f2.seek(0)

  data = int(f1.read()[:-1])
  if data != olddata:
      # print("data1", end=" ")
      # print(data)
      if data > olddata:
          x+=1
          grid[y % yMax][x % xMax] = '*'
          print_grid(grid)
          led_matrix_update(grid)
      elif data < olddata:
          x-=1
          grid[y % yMax][x % xMax] = '*'
          print_grid(grid)
          led_matrix_update(grid)
      olddata = data

  data = int(f2.read()[:-1])
  if data != olddata2:
      # print("data2", end=" ")
      # print(data)
      if data > olddata2:
          y+=1
          grid[y % yMax][x % xMax] = '*'
          print_grid(grid)
          led_matrix_update(grid)
      elif data < olddata2:
          y-=1
          grid[y % yMax][x % xMax] = '*'
          print_grid(grid)
          led_matrix_update(grid)
      olddata2 = data
  time.sleep(ms/1000)

  # push buttons

  # if GPIO.input("P8_13") == 1:
  #   print("HIGH 11")
  #   y-=1
  #   grid[y % yMax][x % xMax] = '*'
  #   print_grid(grid)
  #   led_matrix_update(grid)
  #   time.sleep(0.2)

  # if GPIO.input("P8_14") == 1:
  #   print("HIGH 13")
  #   y+=1
  #   grid[y % yMax][x % xMax] = '*'
  #   print_grid(grid)
  #   led_matrix_update(grid)
  #   time.sleep(0.2)

  # if GPIO.input("P8_15") == 1:
  #   print("HIGH 19")
  #   x-=1
  #   grid[y % yMax][x % xMax] = '*'
  #   print_grid(grid)
  #   led_matrix_update(grid)
  #   time.sleep(0.2)

  # if GPIO.input("P8_17") == 1:
  #   print("HIGH 17")
  #   x+=1
  #   grid[y % yMax][x % xMax] = '*'
  #   led_matrix_update(grid)
  #   print_grid(grid)
  #   time.sleep(0.2)

# Keyboard input

# while True:
#   read = input("Enter a command: ")
#   read = read.strip().lower()

#   if read == 'q':
#     print("Quitting...")
#     break
#   elif read == 'u':
#     y-=1
#   elif read == 'd':
#     y+=1
#   elif read == 'l':
#     x-=1
#   elif read == 'r':
#     x+=1
#   elif read == 'c':
#     grid = [['.' for i in range(xMax)] for j in range(yMax)]
#     x = 0
#     y = 0
#   else:
#     print("Invalid command entered.")
#     print(read)

#   grid[y % yMax][x % xMax] = '*'
#   print_grid(grid)
