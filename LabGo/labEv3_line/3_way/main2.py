#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait,DataLog, StopWatch
from pybricks.robotics import DriveBase

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)
data = DataLog("Time","Angle")
watch = StopWatch()
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 9
WHITE = 65
threshold = (BLACK + WHITE) / 2


check = True
# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 150

PROPORTIONAL_GAIN = 1.4 # 1.2

# Start following the line endlessly.
while True:
    if line_sensor.color() == Color.GREEN :
        while line_sensor.color() != Color.RED:
            # Calculate the deviation from the threshold.
            error = line_sensor.reflection() - threshold
            if error > 18: #10-15
                DRIVE_SPEED = 90
                PROPORTIONAL_GAIN = 3.7
            else:
                DRIVE_SPEED = 120
                PROPORTIONAL_GAIN = 1.4
                
            # Calculate the turn rate.
            turn_rate = PROPORTIONAL_GAIN * error

            # Set the drive base speed and turn rate.
            robot.drive(DRIVE_SPEED, turn_rate)
            angle = left_motor.angle()
            time = watch.time()
            data.log(time,angle)
            # You can wait for a short time or do other things in this loop.
            wait(10)

        check = False
        break
    else :
        continue