import RPi.GPIO as GPIO
import motor_config as mcfg
import motor

class Car:
    motors = {}

    def __init__(self):
        # Add motors
        mcfg.init(self)
        return

    def __del__(self):
        GPIO.cleanup()
        return

    def addDC(self, name, GPIOin1, GPIOin2, GPIOen, speed=10):
        self.motors[name] = motor.DC(name, GPIOin1, GPIOin2, GPIOen, speed)
        return

    def addServo(self, name, GPIOin, speed=10):
        self.motors[name] = motor.Servo(name, GPIOin, speed=2.5)
        return

    def printMotors(self):
        print(self.motors)
        return

