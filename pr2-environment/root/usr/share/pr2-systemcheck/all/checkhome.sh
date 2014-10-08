#!/bin/sh

space=`df /home --total | tail -n1 | awk '{print $5}' | sed -re 's/([0-9]*)\%/\1/'`

if [ ${space} -ge 90 ]; then
    echo "Home directory is ${space}% full" >&2
    exit 1
fi

mount | grep -q "/dev/mapper/vg00-home on /home" || {
    echo "Home is not mounted from /dev/mapper/vg00-home.  Check that LVM is set up correctly" >&2
    exit 1
}

exit 0