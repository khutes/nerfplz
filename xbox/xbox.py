#This program detects input from the controller and prints it to the screen.
#Next step, each input will call a specific function that controls the motors. 
#Integrate this with networking and camera 
import pygame
import controller
import time

def run(socket):
	pygame.init()

	REFRESH_RATE = 20

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	#Creates a pygame screen, only required to pick up input from the xbox controller
	screen = pygame.display.set_mode((100,100))

	# make a controller
	cont = controller.Controller()

	# Game Loop
	done = False
	test = input("Enter anything: ")
	socket.send(test)

	while done==False:
	# event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
			# handle events for specific buttons
			if event.type == pygame.JOYBUTTONDOWN: #add button up
				if event.button == controller.A:
					print("A Button Down")
					socket.send("A Button Down")					
				if event.button == controller.B:
					print("B Button Down")
				if event.button == controller.X:
					print("X Button Down")
				if event.button == controller.Y:
					print("Y Button Down")
				if event.button == controller.LEFT_BUMP:
					print("Left Bump Button Down")
				if event.button == controller.RIGHT_BUMP:
					print("Right Bump Button Down")		
				if event.button == controller.BACK:
					print("Quiting...")				
					done=True					
			# handle events for specific buttons
			if event.type == pygame.JOYBUTTONUP: #add button up
				if event.button == controller.A:
					print("A Button Up")
				if event.button == controller.B:
					print("B Button Up")
				if event.button == controller.X:
					print("X Button Up")
				if event.button == controller.Y:
					print("Y Button Up")
				if event.button == controller.LEFT_BUMP:
					print("Left Bump Button Up")
				if event.button == controller.RIGHT_BUMP:
					print("Right Bump Button Up")			
		# handle joysticks
		left_x, left_y = cont.get_left_stick()
		if left_x > 0.5 :
			print("Turn Right")
			time.sleep(0.1)
		if left_x < -0.5 :
			print("Turn Left")
			time.sleep(0.1)
		if left_y > 0.5 :
			print("Backward")
			time.sleep(0.1)
		if left_y < -0.5 :
			print("Forward")
			time.sleep(0.1)

		right_x, right_y = cont.get_right_stick()
		if right_x > 0.5 :
			print("Steer Right")
			time.sleep(0.1)
		if right_x < -0.5 :
			print("Steer Left")
			time.sleep(0.1)
		if right_y > 0.5 :
			print("Steer Down")
			time.sleep(0.1)
		if right_y < -0.5 :
			print("Steer Up")
			time.sleep(0.1)

		trigger = cont.get_triggers()
		if trigger > 0.3 :
			print("Right Trigger")
			time.sleep(0.1)
		if trigger < -0.3 :
			print("Left Trigger")
			time.sleep(0.1)

		dpad = cont.get_pad() # up, right, down, left
		if dpad[0] == 1 :
			print("D-PAD UP")
			time.sleep(0.1)
		if dpad[1] == 1 :
			print("D-PAD RIGHT")
			time.sleep(0.1)
		if dpad[2] == 1 :
			print("D-PAD DOWN")
			time.sleep(0.1)
		if dpad[3] == 1 :
			print("D-PAD LEFT")
			time.sleep(0.1)
