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
                         