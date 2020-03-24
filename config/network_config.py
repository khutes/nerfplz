import socket

"""
This config file would have the credentials of remote server, 
the commands to execute, upload and download file path details.
"""

#Server credential details needed for ssh 
HOST = ''
HOSTNAME = 'nerfpi'
USERNAME='pi'
PASSWORD='pi'
PORT = 22
MESSAGE_PORT = 8080
TIMEOUT = 10

#.pem file details
# PKEY = 'Enter your key filename here'

#Sample commands to execute(Add your commands here)
COMMANDS = ['python3 ~/Desktop/nerfplz/rpi.py']

def init():
    global HOST
    HOST = socket.getaddrinfo("nerfpi", None, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0]
    print("RPI Address: " + HOST)
    return 0

def test():
    global HOST
    HOST = "fe80::37ed:7061:ac73:1b95"
    # HOST = "10.183.166.148"
    # print(socket.getaddrinfo("nerfpi", None, family=socket.AF_INET, proto=socket.IPPROTO_TCP))
