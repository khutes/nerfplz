import socket

"""
This config file would have the credentials of remote server, 
the commands to execute, upload and download file path details.
"""

#Server credential details needed for ssh 
HOST = ''
HOSTNAME = 'raspberrypi'
USERNAME='pi'
PASSWORD='raspberry'
PORT = 22
MESSAGE_PORT = 8080
CAMERA_PORT = 8000
TIMEOUT = 10
ALIVE = True

#.pem file details
# PKEY = 'Enter your key filename here'

#Sample commands to execute(Add your commands here)
COMMANDS = ['python3 ~/Desktop/nerfplz/rpi.py']

def init():
    global HOST
    HOST = socket.getaddrinfo(HOSTNAME, None, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0]
    print("RPI Address: " + HOST)
    return 0
