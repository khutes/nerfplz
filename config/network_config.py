"""
This config file would have the credentials of remote server, 
the commands to execute, upload and download file path details.
"""
#Server credential details needed for ssh 
HOST='192.168.1.8'
USERNAME='pi'
PASSWORD='pi'
PORT = 22
MESSAGE_PORT = 8080
TIMEOUT = 10

#.pem file details
# PKEY = 'Enter your key filename here'

#Sample commands to execute(Add your commands here)
COMMANDS = ['python3 ~/Desktop/nerfplz/rpi.py']
