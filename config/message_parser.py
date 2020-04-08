"""
Function will be used to parse through the message recieved by the Pi and 
perform the task indicated. 
"""

def parse(car, msg):
	if msg == "fire":
		car.fire()
	elif msg == "quit":
		print("quit")
	else:
		value = int(msg[2:])
		if "fd" in msg:
			car.driveForward(value)
		elif "tl" in msg:
			car.steerLeft(value)		
		elif "bd" in msg:
			car.driveBackward(value)		
		elif "tr" in msg:
			car.steerRight(value)		
		elif "cu" in msg:
			car.lookUp(value)		
		elif "cl" in msg:
			car.lookLeft(value)		
		elif "cd" in msg:
			car.lookDown(value)		
		elif "cr" in msg:
			car.lookRight(value)		
		else:
			print("wrong input")
