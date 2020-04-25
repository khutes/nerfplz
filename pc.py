from config import network_config as cfg
from config import messages_config as msgcfg
from config import controller_config as xboxCont
from network import network
from network import ssh
from controls import xbox
from controls import keyboard
import pygame
import webbrowser
import time
import threading

threads = []

# Find the pi on the network
while True: # Change to True
    try:
        cfg.init()
    except Exception as e:
        print("Error obtaining raspberry pi address. Retrying...")
        continue
    # Starting scripts on the pi
    try:  
        ssh.execute()
        break
    except Exception as e:
        print("Error starting server on raspberry pi. Retrying...")

try:

    print("Connecting messaging client..")
    socket = network.createMessageClient()
    msgcfg.setSocket(socket)

    try:
        cont = xboxCont.Controller()
        print("Using xbox controller...")
        t = threading.Thread(target=xbox.run, args=(cont,))
        threads.append(t)
        t.start()
    except Exception as e:
        print("No xbox controller detected\nUsing keyboard controls...")
        print("Using keyboard...")
        t = threading.Thread(target = keyboard.run)
        threads.append(t)
        t.start()

    # Creating the camera feed
    print("Opening camera feed...")
    camURL = "http://[" + str(cfg.HOST) + "]:" + str(cfg.CAMERA_PORT)
    # webbrowser.open(camURL)

except Exception as e:
    print("Error operating client: " + str(e))
    print("Shutting down system...")

print("Waiting for system shutdown...")
for t in threads:
    t.join()
    
