import RPi.GPIO as GPIO
from config import motor_config as mcfg
import time

GPIO.setmode(GPIO.BCM)

class DC:
    def __init__(self, name, GPIOin1, GPIOin2, GPIOen, speed, minS, maxS):
        self.name = name
        self.in1 = GPIOin1
        self.in2 = GPIOin2
        self.en = GPIOen
        self.speed = speed
        self.increment = mcfg.DC_SPEED_INC
        
        self.minSpeed = minS
        self.maxSpeed = maxS

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p = GPIO.PWM(self.en, mcfg.DEFAULT_HERTZ)
        self.p.start(self.speed)
        self.p.ChangeDutyCycle(0)
        return

    def __del__(self):
        self.p.stop()

    def fwd(self, speed=None):
        if speed is not None and speed > 0:
            self.setSpeed(int(100 * speed))
        self.p.ChangeDutyCycle(self.speed)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        return

    def bckwd(self, speed=None):
        if speed is not None and speed > 0:
            self.setSpeed(int(100 * speed))
        self.p.ChangeDutyCycle(self.speed)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in1, GPIO.HIGH)
        return

    def setSpeed(self, speed):
        self.speed = speed
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed < self.minSpeed:
            self.speed = self.minSpeed
        print("%s speed set to %.0f" % (self.name, self.speed)) 
        return
    
    def setSpeedLimits(self, minSpeed, maxSpeed):
        if (minSpeed > 0 and minSpeed < maxSpeed):
            self.minSpeed = minSpeed
        if (maxSpeed < 100 and maxSpeed > minSpeed):
            self.maxSpeed = maxSpeed
        return
    
    def setIncrement(self, increment):
        self.increment = increment
        return

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p.ChangeDutyCycle(0)
        return


class Servo:
    
    def __init__(self, name, GPIOpin, angle, minAngle, maxAngle, increment):
        self.name = name
        self.pin = GPIOpin
        self.increment = increment

        self.minAngle = minAngle
        self.maxAngle = maxAngle
        self.setAngle(angle)
        dutyCycle = self.angle / 18 + 2.5

        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, mcfg.DEFAULT_HERTZ)
        self.p.start(dutyCycle)
        self.p.ChangeDutyCycle(0)
        return

    def __del__(self):
        self.p.stop()

    def fwd(self, increment=None):
        if increment is not None and increment > 0:
            self.setAngle(self.angle + increment * self.increment)
        else:
            self.setAngle(self.angle + self.increment)
        dutyCycle = self.angle / 18 + 2.5
        self.p.ChangeDutyCycle(dutyCycle)
        return

    def bckwd(self, increment=None):
        if increment is not None and increment > 0:
            self.setAngle(self.angle - increment * self.increment)
        else:
            self.setAngle(self.angle - self.increment)
        dutyCycle = self.angle / 18 + 2.5
        self.p.ChangeDutyCycle(dutyCycle)
        return

    def setAngle(self, angle):
        self.angle = angle
        if self.angle > self.maxAngle:
            self.angle = self.maxAngle
        elif self.angle < self.minAngle:
            self.angle = self.minAngle
        print("%s angle set to %.0f out of %.0f" % (self.name, self.angle, self.maxAngle))
        return

    def setAngleLimits(self, minAngle, maxAngle):
        if (minAngle > 0 and minAngle < maxAngle):
            self.minAngle = minAngle
        if (maxAngle < 180 and maxAngle > minAngle):
            self.maxAngle = maxAngle
        return
    
    def setIncrement(self, increment):
        self.increment = increment
        return

    def stop(self):
        time.sleep(.1)
        self.p.ChangeDutyCycle(0)
        return
