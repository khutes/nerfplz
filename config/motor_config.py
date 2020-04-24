

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 90
DC_MIN_SPEED = 25
DC_SPEED_INC = 2.5

SERVO_MIN_ANGLE = 45
SERVO_MAX_ANGLE = 135
SERVO_ANGLE_INC = 5

def init(car):
    # car.addDC("BackMotor", 24, 23, 25, 50)
    car.addServo("FrontServo", 17, 90)
    # Add motors here as desired
    car.printMotors()
    return
