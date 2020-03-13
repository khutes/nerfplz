import network
import ssh

# network.createClient()
ssh.execute()

# try:
network.createClient()

# except Exception as e:
#     print("Socket error: " + str(e))

# finally:
ssh.killServer()