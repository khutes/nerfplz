#This program detects input from the controller and prints it to the screen.
#Next step, each input will call a specific function that controls the motors. 
#Integrate this with networking and camera 
import pygame
import time
from config import messages_config as send_to_pi

def run():
	pygame.init()

	done = False
	# Creates a pygame screen, only required to pick up input from the xbox controller
	screen = pygame.display.set_mode((100,100))

	try:	
		while done == False:
		# event handling
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				send_to_pi.messages(1, 0.5)
				time.sleep(0.1)				
			if keys[pygame.K_a]:
				send_to_pi.messages(2, 1.0)
				time.sleep(0.1)					
			if keys[pygame.K_s]:
				send_to_pi.messages(3, 0.5)
				time.sleep(0.1)					
			if keys[pygame.K_d]:
				send_to_pi.messages(4, 1.0)
				time.sleep(0.1)					
			if keys[pygame.K_UP]:
				send_to_pi.messages(5, 0.5)
				time.sleep(0.1)					
			if keys[pygame.K_LEFT]:
				send_to_pi.messages(6, 0.5)
				time.sleep(0.1)					
			if keys[pygame.K_DOWN]:
				send_to_pi.messages(7, 0.5)
				time.sleep(0.1)					
			if keys[pygame.K_RIGHT]:
				send_to_pi.messages(8, 0.5)
				time.sleep(0.1)					
			if keys[pygame.K_SPACE]:
				send_to_pi.messages(9, 0)
				time.sleep(0.1)					
			pygame.event.pump()			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					send_to_pi.messages(0, 0)
					done=True
	except KeyboardInterrupt:
		pygame.quit()
		send_to_pi.messages(0, 0)
