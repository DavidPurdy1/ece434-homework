#!/bin/bash

# Shows different media on the screen

# Just in case
export SDL_VIDEODRIVER=fbcon
export SDL_FBDEV=/dev/fb0

echo "Press enter to move between different media"
echo "Image first"
sudo fbi -noverbose -T 1 -a media/bird.jpeg

read -p "Press enter to continue" -n 1 -s
echo ""

echo "Video next"
mplayer -vo fbdev2 -nolirc -framedrop media/cat.mp4

read -p "Press enter to continue" -n 1 -s
echo ""

echo "Text next"
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'David Purdy\nIm the biggest\nbird' \
     -draw "text 0,200 ''" \
     $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE