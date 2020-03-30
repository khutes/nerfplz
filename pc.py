from config import network_config as cfg
from network import network
from network import ssh
import webbrowser
import time
import threading

threads = []

while True:
    try:
        cfg.init()
        break
    except Exception as e:
        print("Error obtaining raspberry pi address. Retrying in 5 seconds...")
        time.sleep(5)

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

    print("Opening camera feed...")
    camURL = "http://[" + str(cfg.HOST) + "]:" + str(cfg.CAMERA_PORT)
    webbrowser.open(camURL)

    print("Connecting messaging client")
    network.createMessageClient()

    webbrowser.close()

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
