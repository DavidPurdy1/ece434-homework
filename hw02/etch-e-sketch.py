#!/usr/bin/python
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
# HW02
# David Purdy 12-12-2022

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

while True:
  if GPIO.input("P8_11") == 1:
    print("HIGH 11")
    y-=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    time.sleep(0.2)

  if GPIO.input("P8_13") == 1:
    print("HIGH 13")
    y+=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    time.sleep(0.2)

  if GPIO.input("P8_19") == 1:
    print("HIGH 19")
    x-=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    time.sleep(0.2)

  if GPIO.input("P8_17") == 1:
    print("HIGH 17")
    x+=1
    grid[y % yMax][x % xMax] = '*'
    print_grid(grid)
    time.sleep(0.2)


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