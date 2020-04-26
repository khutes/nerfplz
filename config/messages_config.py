
__sock = None

def setSocket(socket):
	global __sock
	__sock = socket

def messages(input, value):
	if input == 0: #Quit
		msg = "quit"	
		__sock.send(msg)	
	if input == 1: #Forward
		# value = int(value*100)
		msg = "fd"+str(value)
		__sock.send(msg)		
	if input == 2: #Turn Left
		# value = int(value*100)
		msg = "tl"+str(value)	
		__sock.send(msg)
	if input == 3: #Backward
		# value = int(value*100)
		msg = "bd"+str(value)
		__sock.send(msg)
	if input == 4: #Turn Right
		# value = int(value*100)
		msg = "tr"+str(value)		
		__sock.send(msg)
	if input == 5: #Camera Up
		# value = int(value*100)
		msg = "cu"+str(value)	
		__sock.send(msg)
	if input == 6: #Camera Left
		# value = int(value*100)
		msg = "cl"+str(value)	
		__sock.send(msg)
	if input == 7: #Camera Down
		# value = int(value*100)
		msg = "cd"+str(value)	
		__sock.send(msg)		
	if input == 8: #Camera Right
		# value = int(value*100)
		msg = "cr"+str(value)	
		__sock.send(msg)
	if input == 9: #Fire
		msg = "fire"	
		__sock.send(msg)
	if input == 10:  #Reset
		msg = "reset"
		__sock.send(msg)