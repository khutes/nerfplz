import RPi.GPIO as GPIO
from config import motor_config as mcfg
from car import motor

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

    def addServo(self, name, GPIOin, angle=10):
        self.motors[name] = motor.Servo(name, GPIOin, angle)
        return

    def driveForward(self, factor):
        # Back motor forward
        print("Called car.driveForward")
        self.motors["BackMotor"].fwd()
        return

    def driveBackward(self, factor):
        # Back motor backward
        print("Called car.driveBackward")
        self.motors["BackMotor"].bckwd()
        return

    def steerLeft(self, factor):
        # Front servo forwrad
        print("Called car.steerLeft")
        self.motors["FrontServo"].fwd()
        return

    def steerRight(self, factor):
        # Front servo backward
        print("Called car.steerRight")
        self.motors["FrontServo"].bckwd()
        return

    def lookLeft(self, factor):
        # Turret servo forward
        print("Called car.lookLeft")
        self.motors["TurretMotor"].fwd()
        return

    def lookRight(self, factor):
        # Turret servo backward
        print("Called car.lookRight")
        self.motors["TurretMotor"].bckwd()
        return

    def lookUp(self, factor):
        # Tilt servo up
        print("Called car.lookUp")
        self.motors["TiltServo"].fwd()
        return

    def lookDown(self, factor):
        # Tilt servo down
        print("Called car.lookDown")
        self.motors["TiltServo"].bckwd()
        return

    def fire(self):
        # Fire motor
        print("Called car.fire")
        self.motors["FireMotor"].fwd()
        return

    def stop(self, motor):
        self.motors[motor].stop()
        return

    def printMotors(self):
        print(self.motors)
        return

