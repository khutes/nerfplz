import RPi.GPIO as GPIO
import motor_config as mcfg

GPIO.setmode(GPIO.BCM)

class DC:
    def __init__(self, name, GPIOin1, GPIOin2, GPIOen, speed):
        self.name = name
        self.in1 = GPIOin1
        self.in2 = GPIOin2
        self.en = GPIOen
        self.speed = speed
        
        self.maxSpeed = mcfg.DEFAULT_MAX_SPEED
        self.minSpeed = mcfg.DEFAULT_MIN_SPEED

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p = GPIO.PWM(self.en, mcfg.DEFAULT_HERTZ)
        self.p.start(self.speed)
        return

    def __del__(self):
        self.p.stop()

    def fwd(self, speed=None):
        if speed is not None:
            self.setSpeed(speed)
        self.p.ChangeDutyCycle(self.speed)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in1, GPIO.HIGH)
        return

    def bckwd(self, speed=None):
        if speed is not None:
            self.setSpeed(speed)
        self.p.ChangeDutyCycle(self.speed)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
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

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        return


class Servo:
    def __init__(self, name, GPIOpin, speed):
        self.name = name
        self.pin = GPIOpin
        self.speed = speed

        self.maxSpeed = mcfg.DEFAULT_MAX_SPEED
        self.minSpeed = mcfg.DEFAULT_MIN_SPEED

        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, mcfg.DEFAULT_HERTZ)
        self.p.start(self.speed)
        return

    def __del__(self):
        self.p.stop()

    def fwd(self, speed=None):
        if speed is not None:
            self.setSpeed(speed)
        self.p.ChangeDutyCycle(self.speed)
        return

    def bckwd(self, speed=None):
        if speed is not None:
            self.setSpeed(speed)
        self.p.ChangeDutyCycle(self.speed)
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

    def stop(self):
        self.p.ChangeDutyCycle(0)
        return
