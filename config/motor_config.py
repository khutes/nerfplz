

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 100
DC_MIN_SPEED = 0
DC_SPEED_INC = 5

# Default angle is 90
SERVO_MIN_ANGLE = 45
SERVO_MAX_ANGLE = 135
SERVO_ANGLE_INC = 1

def init(car):
    # name, in1, in2, ena, init speed, min speed, max speed
    car.addDC("BackMotor", GPIOin1=20, GPIOin2=16, GPIOen=21,
              speed=60, minS=15, maxS=75)  # Flipped directions

    car.addDC("TurretMotor", GPIOin1=19, GPIOin2=13, GPIOen=26, speed=15)

    car.addDC("FireMotor", GPIOin1=6, GPIOin2=5,
              GPIOen=14, speed=100, minS=15)

    # name, GPIO, init angle, min angle, max angle, increment
    car.addServo("FrontServo", GPIOpin=17, minAngle=55, maxAngle=125, increment=5)
    
    car.addServo("TiltServo", GPIOpin=27, minAngle=75)

    car.printMotors()
    return
