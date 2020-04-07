from config import network_config as cfg
from network import network
from network import ssh
from xbox import xbox
from keyboard import keyboard
import webbrowser
import time
import threading

threads = []

# Find the pi on the network
while True:
    try:
        cfg.init()
        break
    except Exception as e:
        print("Error obtaining raspberry pi address. Retrying in 5 seconds...")
        time.sleep(5)

# Starting scripts on the pi
while True:
    try:
        ssh.execute()
        break
    except Exception as e:
        print("Error starting server on raspberry pi. Retrying in 5 seconds...")
        time.sleep(5)

try:
    # print("Connecting messaging client...")
    # t = threading.Thread(target = network.createMessageClient)
    # threads.append(t)
    # t.start()

    # Creating the camera feed
    print("Opening camera feed...")
    time.sleep(1)
    camURL = "http://[" + str(cfg.HOST) + "]:" + str(cfg.CAMERA_PORT)
    webbrowser.open(camURL)

    print("Connecting messaging client..")
    socket = network.createMessageClient()

    print("Connecting xbox...")
    t = threading.Thread(target = xbox.run, args=(socket,))
    threads.append(t)
    t.start()
	
    print("Connecting keyboard...")
    t = threading.Thread(target = keyboard.run, args=(socket,))
    threads.append(t)
    t.start()	

    # print("Connecting to Pi Camera...")
    # camSock = network.createCameraClient()
    # print("Connected.  Starting feed...")
    # camClient.viewCameraFeed(camSock)

except Exception as e:
    print("Error operating client: " + str(e))
    print("Shutting down system...")

print("Collecting threads...")
for t in threads:
    t.join()
    
# This option exists if we want to kill the server forcibly from the pc
# Currently it should all be handled from the rpi 
# try:
#     ssh.killServer()
# except Exception as e:
#     print("Error killing server on RPI\nWARNING: Processes may still be running on RPI")
