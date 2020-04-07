
__sock = None

def set__sock(__sock):
	__sock = __sock

def messages(input, value):
	if input == 0: #Quit
		msg = "quit"	
		print(msg)
		__sock.send(msg)	
	if input == 1: #Forward
		msg = "fd"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)		
	if input == 2: #Turn Left
		msg = "tl"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)
	if input == 3: #Backward
		msg = "bd"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)
	if input == 4: #Turn Right
		msg = "tr"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)
	if input == 5: #Camera Up
		msg = "cu"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)
	if input == 6: #Camera Left
		msg = "cl"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)
	if input == 7: #Camera Down
		msg = "cd"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)		
	if input == 8: #Camera Right
		msg = "cr"+"{:.1f}".format(value)	
		print(msg)
		__sock.send(msg)
	if input == 9: #Fire
		msg = "fire"	
		print(msg)
		__sock.send(msg)