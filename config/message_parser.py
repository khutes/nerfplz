from config import network_config as cfg


"""
Function will be used to parse through the message recieved by the Pi and 
perform the task indicated. 
"""

def parse(sock, car):

    # Move this block into a new module/thread before starting camera feed
    while True:
        try:
            msg = sock.receive()

            if msg == "fire":
                car.fire()
            elif msg == "quit":
                print("quit")
            else:
                value = int(msg[2:])
                if "fd" in msg:
                    if value == 0:
                        car.stop("BackMotor")
                    else:
                        car.driveForward(value)
                elif "tl" in msg:
                    if value == 0:
                        car.stop("FrontServo")
                    else:
                        car.steerLeft(value)
                elif "bd" in msg:
                    if value == 0:
                        car.stop("BackMotor")
                    else:
                        car.driveBackward(value)
                elif "tr" in msg:
                    if value == 0:
                        car.stop("FrontServo")
                    else:
                        car.steerRight(value)
                elif "cu" in msg:
                    if value == 0:
                        car.stop("TiltServo")
                    else:
                        car.lookUp(value)
                elif "cl" in msg:
                    if value == 0:
                        car.stop("TurretMotor")
                    else:
                        car.lookLeft(value)
                elif "cd" in msg:
                    if value == 0:
                        car.stop("TiltServo")
                    else:
                        car.lookDown(value)
                elif "cr" in msg:
                    if value == 0:
                        car.stop("TurretMotor")
                    else:
                        car.lookRight(value)
                else:
                    print("wrong input")
        except:
            cfg.ALIVE = False
            print("Error. Closing connection...")
            del sock
            break


