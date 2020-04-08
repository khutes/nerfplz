import RPi.GPIO as GPIO
from config import motor_config as mcfg
from motor import Motor

class Car:
    motors = {}

    def __init__(self):
        # Add motors
        mcfg.init(self)
        return

    def __del__(self):
        GPIO.cleanup()
        return

    def addMotor(self, name, GPIOin1, GPIOin2, GPIOen, speed=10):
        self.motors[name] = Motor(name, GPIOin1, GPIOin2, GPIOen, speed)
        return

    def printMotors(self):
        print(self.motors)
        return

