#!/bin/sh

. /etc/ros/fuerte/setup.sh

if [ $# -eq 0 ] ; then
    /bin/echo "Entering environment at /opt/ros/fuerte"
    $SHELL
    /bin/echo "Exiting build environment at /opt/ros/fuerte"
else
    exec "$@"
fi



