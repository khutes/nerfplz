#This program detects input from the controller and prints it to the screen.
#Next step, each input will call a specific function that controls the motors. 
#Integrate this with networking and camera 
import pygame
import time
from config import controller_config as controller
from config import messages_config as send_to_pi


def run():
	pygame.init()

	# REFRESH_RATE = 20

	# # Used to manage how fast the screen updates
	# clock = pygame.time.Clock()

	#Creates a pygame screen, only required to pick up input from the xbox controller
	screen = pygame.display.set_mode((100,100))

	# make a controller
	cont = controller.Controller()

	# Game Loop
	done = False
	# for testing purposes
	# test = input("Enter anything: ")
	# send_to_pi.messages(9, 0)

	while done==False:
	# event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				send_to_pi.messages(0,0)
				done=True
			# handle events for specific buttons
			if event.type == pygame.JOYBUTTONDOWN: #add button up
				if event.button == controller.RIGHT_BUMP: #Fire
					send_to_pi.messages(9,0)		
				if event.button == controller.BACK: #Quit
					send_to_pi.messages(0,0)				
					done=True					

		trigger = cont.get_triggers()
		if trigger > 0.2 : #Right Trigger
			send_to_pi.messages(1,trigger)
			time.sleep(0.1)
		else:
			send_to_pi.messages(1, 0)
			time.sleep(0.1)
		if trigger < -0.3 : #Left Trigger
			send_to_pi.messages(3,trigger)
			time.sleep(0.1)
		else:
			send_to_pi.messages(3, 0)
			time.sleep(0.1)
			
		# handle joysticks
		left_x, left_y = cont.get_left_stick()
		if left_x > cont.dead_zone:  # Turn Right
			send_to_pi.messages(4,left_x)
			time.sleep(0.1)
		elif left_x < -cont.dead_zone: #Turn Left
			send_to_pi.messages(2,left_x)
			time.sleep(0.1)
		else:
			send_to_pi.messages(2, 0)
			time.sleep(0.1)

		right_x, right_y = cont.get_right_stick()
		if right_x > cont.dead_zone:  # Camera Right
			send_to_pi.messages(8,right_x)
			time.sleep(0.1)
		elif right_x < -cont.dead_zone:  # Camera Left
			send_to_pi.messages(6,right_x)
			time.sleep(0.1)
		else:
			send_to_pi.messages(8, 0)
			time.sleep(0.1)

		if right_y > cont.dead_zone:  # Camera Down
			send_to_pi.messages(7,right_y)
			time.sleep(0.1)
		elif right_y < -cont.dead_zone:  # Camera Up
			send_to_pi.messages(5,right_y)
			time.sleep(0.1)
		else:
			send_to_pi.messages(7, 0)
			time.sleep(0.1)
