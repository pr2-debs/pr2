#!/bin/sh

lsusb | grep 045e:02ae > /dev/null

if [ ${?} -eq 0 ]; then
    echo "Found Kinect Sensor"
    exit 0
else
    lsusb | grep 1d27:0600 > /dev/null
    if [ ${?} -eq 0 ] ; then
       echo "Found Asus Sensor"
       exit 0
    fi
fi

echo "No Kinect/Asus sensors found" >&2
exit 2
