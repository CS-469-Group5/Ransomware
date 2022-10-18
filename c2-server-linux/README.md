# C2 Server - Linux Target

## NOTE - Still a work in progress

### What Is This?
This uses secure sockets to connect to a client and perform a reverse shell.

### How To Use

Generate the keys for SSL: ```sh ssl/generate_key.sh```

For localhost:

Start the server: ```python3 server.py 0.0.0.0```

Start the client: ```python3 client.py 0.0.0.0```

Commands can now be issued from the server on the client.


