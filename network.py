import socket
import time


class CustomSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        totalsent = 0
        MSGLEN = len(msg)
        msg = str(MSGLEN) + "x" + msg
        msg = msg.encode()
        MSGLEN = len(msg)
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        chunks = []
        bytes_recd = 0
        MSGLEN = 2
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CustomSocket = CustomSocket(s)

hostname = socket.gethostname()
address = socket.gethostbyname(hostname)
# print("Host Name: " + hostname + "\nAddress: " + address)

piAddress = socket.gethostbyname("raspberrypi")
# print("Pi Address: " + piAddress)

CustomSocket.connect(piAddress, 8080)

while True:
    msg = input("What message do you want to send?\n\nEnter: ")
    CustomSocket.send(msg)
    print("message sent\n")
