#============================================================
#
#                         Project 1
#               CSE 4360 - Robotics 
#            The University of Texas at Arlington
#            
#============================================================
#            Authors:
#            Preston Mann 1001677983 
#            Bryan Nguyen 1001719605
#============================================================
#
# File: main.py
#
# Brief: This file is the main has the movement functions for 
#        the robot to move around the course
#        it has 90 degree turns and 45 degree turns
#        it also has 90 degree forward and backward movements
#        it also has 45 degree forward and backward movements
#        left motor is port C right motor is port A 
#
# Revision History:
# Date       | Engineer     | Description
# -----------|--------------|--------------------------------
# 11-2-2022  | Bryan, N     | Initial Release
# 11-2-2022  | Preston, M   | Initial Release
#
#============================================================
#TODO:
# make motor class to make code more modular
from const import * 
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

import time

left_motor  = Motor(Port.C)
right_motor = Motor(Port.A)

def turn_left90():
    right_motor.run_time(  -turning_speed-0,  turning_time+off_set90,  Stop.HOLD, False)
    left_motor.run_time(  turning_speed,  turning_time + off_set90,  Stop.HOLD, True)
    time.sleep(1)

def turn_right90():
    #subtract top for down offset and bot for up offset 
    right_motor.run_time(   turning_speed,  turning_time+off_set90,  Stop.HOLD, False)
    left_motor.run_time( -turning_speed,  turning_time+off_set90,  Stop.HOLD, True)
    time.sleep(1)


def turn_left45():
    right_motor.run_time(  -turning_speed,  (turning_time/2)+off_set45,  Stop.HOLD, False)
    left_motor.run_time(  turning_speed,  (turning_time/2)+off_set45,  Stop.HOLD, True)
    time.sleep(1)


def turn_right45():
    right_motor.run_time(   turning_speed,  (turning_time/2)+off_set45,  Stop.HOLD, False)
    left_motor.run_time( -turning_speed,  (turning_time/2)+off_set45,  Stop.HOLD, True)
    time.sleep(1)

def move_forward90():
    left_motor.run_time(   movement_speed, movement_time90, Stop.HOLD, False)
    right_motor.run_time(  movement_speed,    movement_time90, Stop.HOLD, True)
    time.sleep(0.5)

def move_backward90():
    left_motor.run_time(  -movement_speed, movement_time90, Stop.HOLD, False)
    right_motor.run_time( -movement_speed,    movement_time90, Stop.HOLD, True)
    time.sleep(0.5)

def move_forward45():
    left_motor.run_time(   movement_speed, movement_time45, Stop.HOLD, False)
    right_motor.run_time(  movement_speed,    movement_time45, Stop.HOLD, True)
    time.sleep(0.5)

def move_backward45():
    left_motor.run_time(  -movement_speed, movement_time45, Stop.HOLD, False)
    right_motor.run_time( -movement_speed,    movement_time45, Stop.HOLD, True)
    time.sleep(0.5)
                         