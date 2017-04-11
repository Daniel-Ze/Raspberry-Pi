#!/bin/sh
#install.sh
#install all components for time-lapse functionality

sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
sudo apt-get install python-picamera
cd /
cd /home/pi
mkdir time-lapse
chmod 755 time-lapse-launcher.sh
cd /
