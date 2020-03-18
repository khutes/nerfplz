

from config import network_config as conf_file
import socket
import paramiko
import os
import sys
import time

class Ssh_Util:
    "Class to connect to remote server"

    def __init__(self):
        self.ssh_output = None
        self.ssh_error = None
        self.client = None
        self.host = conf_file.HOST
        self.username = conf_file.USERNAME
        self.password = conf_file.PASSWORD
        self.timeout = float(conf_file.TIMEOUT)
        self.commands = conf_file.COMMANDS
        # self.pkey = conf_file.PKEY
        self.port = conf_file.PORT

    def connect(self):
        "Login to the remote server"
        try:
            #Paramiko.SSHClient can be used to make connections to the remote server and transfer files
            print("Establishing ssh connection...")
            self.client = paramiko.SSHClient()
            #Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #Connect to the server
            self.client.connect(hostname=self.host, port=self.port, username=self.username,
                                password=self.password, timeout=self.timeout, allow_agent=False, look_for_keys=False)
            print("Connected to the server", self.host)
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
            result_flag = False
        except paramiko.SSHException as sshException:
            print("Could not establish SSH connection: %s" % sshException)
            result_flag = False
        except socket.timeout as e:
            print("Connection timed out")
            result_flag = False
        except Exception as e:
            print('\nException in connecting to the server')
            print('PYTHON SAYS:', e)
            result_flag = False
            self.client.close()
        else:
            result_flag = True

        return result_flag

    def execute_command(self, commands):
        """Execute a command on the remote host. Return a tuple containing
        an integer status and a two strings, the first containing stdout
        and the second containing stderr from the command."""
        self.ssh_output = None
        result_flag = True
        try:
            if self.connect():
                for command in commands:
                    print("Executing command --> {}".format(command))
                    stdin, stdout, stderr = self.client.exec_command(command, timeout=5)
                    self.ssh_output = stdout.read()
                    self.ssh_error = stderr.read()
                    if self.ssh_error:
                        print("Error: " + str(self.ssh_error.decode()))
                        result_flag = False
                    # else:
                        # print("Output: ", command)
                self.client.close()
            else:
                print("Could not establish SSH connection")
                result_flag = False
        except socket.timeout:
            # print("Command timed out.", command)
            self.client.close()
            result_flag = False
        except paramiko.SSHException:
            print("Failed to execute the command!", command)
            self.client.close()
            result_flag = False

        return result_flag


# Executes commands from network_config file
def execute():

    #Initialize the ssh object
    ssh_obj = Ssh_Util()

    #Execute commands
    if ssh_obj.execute_command(ssh_obj.commands) is True:
        return

# Shut down processes on raspberry pi to clear up ports
def killServer():
    #Initialize the ssh object
    ssh_obj = Ssh_Util()

    # Execute commands
    if ssh_obj.execute_command(["killall -9 python3"]) is True:
        return

