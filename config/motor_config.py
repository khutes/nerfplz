

DEFAULT_HERTZ = 50


def init(car):
    car.addMotor(
        "test",
        24,
        23,
        25,
        50
    )
    # Add motors here as desired
    car.printMotors()
    return
