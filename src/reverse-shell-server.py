from socket import *

# ASCII Art for Samuel
samuel_ascii = """
   .-""-.
  /      \\
 |        |
  \\      /
   '-..-'
    |  |
   /    \\
  |      |
   \\    /
    '----'
     Samuel
"""

print(samuel_ascii)
print('Server listening and awaiting instructions')

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM) # create socket IPv4 & TCP
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # allowing the OS to reuse a recently used socket

serverSocket.bind(('',serverPort)) # use IP address computer & serverPort 8000
serverSocket.listen(1) # listening to connections | 1 - number of connections
connectSocket, address = serverSocket.accept() # accept connection

print(f'Connect: {str(address)}')
mes = connectSocket.recv(1024)
print(mes)

command = ''
print('Command sending mode is available. Enter "x" to exit.\n')
while command != 'x': # x = exit
    command = input('>> ')
    try:
        connectSocket.send(command.encode())
        mes = connectSocket.recv(1024).decode()
        print(mes)
    except BrokenPipeError:
        print("Connection lost. Exiting.")
        break
    except Exception as e:
        print(f"Error: {e}")
        break

try:
    connectSocket.shutdown(SHUT_RDWR) # shutdown
except OSError:
    pass  # Socket already closed
connectSocket.close()
