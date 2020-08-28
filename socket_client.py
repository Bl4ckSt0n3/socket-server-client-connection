# import libraries
import socket

#define host and port
host_address = '127.0.0.1'
port_number = 65432

# the steps of client socket: socket -> connect -> recv

def client_connection():

    # creating a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        # connect to server using host_address and port_number
        soc.connect((host_address, port_number))
        # send data byte level
        soc.sendall(b'Hello, client !')
        data = soc.recv(1024)
    # print message on terminal
    print("Recieved data from {}".format(repr(data)))


# start function
client_connection()
