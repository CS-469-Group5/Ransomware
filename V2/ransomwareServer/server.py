import socket
import sys
import ssl
import _thread
import uuid

# constants
SERVER_HOST = sys.argv[1] # "0.0.0.0" for localhost
SERVER_PORT = 5051
BUFFER_SIZE = 1024

key = "priv.pem"
certificate = "cert.crt"


def newClient(client_socket, addr):
    while True:
        #clientID = client_socket.recv(BUFFER_SIZE).decode('ISO-8859-1')
        clientID = client_socket.recv(BUFFER_SIZE)
        clientID = uuid.UUID(bytes=clientID)
        clientID = str(clientID)
        clientKey = client_socket.recv(BUFFER_SIZE).decode('ISO-8859-1')
        clientKey = str(clientKey)
        filename = f"{clientID}.txt"
        if(clientKey):
            with open(filename, 'w') as f:
                f.write(f"{clientID}\n{clientKey}")
            break  
    client_socket.close()
def main():

    '''
    create socket object
    bind the socket to all IP addresses of this host
    begins listening for connection and accepts when a connection is found
    '''
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    s_ssl = ssl.wrap_socket(s, keyfile=key, certfile=certificate, server_side=False)

    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    while True:
        client_socket, client_address = s_ssl.accept()
        print(f"Connected to {client_address[0]}:{client_address[1]}!")
        _thread.start_new_thread(newClient, (client_socket, client_address))

if __name__ == "__main__":
    main()
