# server.py 
import socket                                         
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name
host = socket.gethostname()                           
port = 9999                                           
# bind to the port
serversocket.bind((host, port))                                  
# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))

    recvmessage = clientsocket.recv(1024)
    #recvID = clientsocket.recv(1024)
    recvlist = recvmessage.split(b"=")
    recvlist[0] += b"="
    recvlist[1] = int.from_bytes(recvlist[1], "big")
    print(recvlist)
    sendmessage = "confirmed"
    
    clientsocket.send(sendmessage.encode('ascii'))
    clientsocket.close()
    #change name to id?
    with open(str(recvlist[1])+'.key', 'wb') as f:
        f.write(recvlist[0])
        #f.write(recvlist[1])
        f.close()