# nerfplz
Project for CSCE462 Spring 20

### The command below will start the system from the user's pc.
### It will search the local network for the Raspberry Pi, then establish an SSH connection
### to start a two servers on the Pi.
### A camera server will be started from the pi and bound to port 8000, using an http server.
### Additionally, a socket system will be setup between the PC client and Pi server to 
### send messages between the two
### All systems will clean themselves up if connection is broken.
### Send "quit" from the client PC to break the connection.

# To start system from pc
$ python pc.py

# To use old camera sysetm
# pip install pillow
# pip install matplotlib




