# C2 Server - Linux Target

## NOTE - Still a work in progress

### What is this?
This is a self-hosted Command-and-Control (C2) server for linux targets that performs a reverse shell on the client.
Once the connection is established, the server-side will be able to use commands on the client-side.

### How To Use
At the moment, a hard coded IP is needed to establish a connection between the server and client.
You can use 0.0.0.0 as your IP address to establish a connection if this is done on your local machine.
If it is between two machines on the same wifi, you can use `ifconfig` to find the private IP addresses.

Once the IP addresses are set, run `python3 server.py` where it will begin listening for a connection.
Afterwards, run `python3 client.py [IP]` to connect the two machines. From the server-side, you should receieve a 
message that says the two are connected as well as the working directory. You have successfully performed a reverse shell and can
issue commands on the client/victim.

### Future Work
* Figure how to check if two machines are on different networks and if they're able to connect
* Create an executable for the client.py to run in background of victim's machine
* Execute code on victim's machine from server
* Develop a web interface using the Flask framework for easier use
* Resolve any unintentional breadcrumbs
* Persist
