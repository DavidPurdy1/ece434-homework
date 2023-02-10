#!/bin/bash
# GPIO aggregator script

AGGREGATOR_PATH=/sys/bus/platform/drivers/gpio-aggregator

# gpio-32-63 is the GPIO chip 1, 0-31 is GPIO chip 0, etc
# 18,19 are the lines for the pins I want to use on chip 1
GPIO_PIN_COMMAND="gpio-32-63 12,13,14,15 gpio-0-31 23,26,27 gpio-64-95 1"

# add gpio-aggregator module to the kernel
echo "Setting up GPIO aggregator junk..."
sudo modprobe gpio-aggregator

cd $AGGREGATOR_PATH
echo "Path: $AGGREGATOR_PATH"

sudo chgrp gpio *
sudo chmod g+rw *
ls -ls

# create a new aggregator
echo "Creating aggregator..."

echo $GPIO_PIN_COMMAND

echo $GPIO_PIN_COMMAND > new_device

sleep 1

# check the aggregator
gpiodetect

echo "Done! Make sure that the chip4 is made"
