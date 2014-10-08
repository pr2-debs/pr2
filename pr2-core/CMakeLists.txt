cmake_minimum_required (VERSION 2.6) 
project(ros_robot)
add_executable(robot robot.cpp)
install_targets(/lib/robot robot)
