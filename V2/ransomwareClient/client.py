import ssl
import socket
import uuid

def makeConnection():
    SERVER_HOST = "127.0.0.1" # "127.0.0.1" for localhost
    SERVER_PORT = 5051  

    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))
    ssl_sock = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='cert.crt')
    return(ssl_sock)    

def sendDatatoServer(sslSock, key):
    #make a UUID based on the host ID and current time
    clientID = uuid.uuid1(1)
    with open("id.id", 'w') as f:
        f.write(str(clientID))
    while True:
        sslSock.send((clientID.bytes))
        sslSock.send((key))
        break    
