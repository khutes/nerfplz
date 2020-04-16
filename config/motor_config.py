

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 90
DC_MIN_SPEED = 25
DC_SPEED_INC = 2.5

SERVO_MIN_SPEED = .1
SERVO_MAX_SPEED = 12
SERVO_SPEED_INC = 0.5

def init(car):
    car.addDC("BackMotor", 24, 23, 25, 50)
    car.addServo("FrontServo", 20, 0)
    # Add motors here as desired
    car.printMotors()
    return
