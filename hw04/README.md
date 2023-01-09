# Homework 4 ECE 434

- [ ] GPIO via mmap
- [ ] GPIO toggling as fast as possible
- [x] i2c via kernel driver
- [x] control LED matrix via browser
- [ ] plug in and control TFT LCD


## GPIO via mmap
1. Write a C or python program that reads from at least two switches and controls two LEDs (the built-in LEDs are fine). The GPIO pins used for the switches need to be from two different GPIO ports. This means you will have to use two separate mmap() calls.

2. Write a C or python program that toggles a GPIO port as fast as it can. Measure the speed with an oscilloscope and compare with your previous measurements. Try toggling with no usleep. Is it faster? 

## i2c via kernel driver
Read tmp101 sensors using the kernel driver
Write a progam that reads the temperature from the kernal driver and prints it to the console.

## control LED matrix via browser
Control led matrix via browser. Have 4 buttons to control up, down, left, right

## plug in and control TFT LCD
1. Display images
2. Play videos
3. Generate text

