#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor , GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()
ultrasonic = UltrasonicSensor(Port.S1)
# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
check = False
box1 = False
box2 = False
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

while True:
    #gyro.reset_angle(0)
    robot.drive(300, 0)
    if ultrasonic.distance() > 200 or check == True :
        box2 = True
        if check == True:
            ev3.speaker.beep()
            robot.straight(-45)
            robot.turn(70)
            robot.straight(-230)
            robot.turn(-70)
            robot.turn(-30)
            robot.straight(30)
            robot.turn(30)
            ev3.speaker.beep()
            break
        else:
            continue
    if ultrasonic.distance() <= 50 :
        box1 = True
        if box2 == True:
            check = True
        else:
            continue

        

