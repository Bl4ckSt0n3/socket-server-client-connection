# import socket library
import socket

# define necessary host and port 
host_address = '127.0.0.1' # localhost
port_number = 65432

# the all steps of socket server side: socket -> bind -> listen -> accept 


def server_connection():

    # first step is creating a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        # the second step, put into bind() host_address and port_number as a 2-tuple 
        soc.bind((host_address, port_number)) 
        # it has to be listen ports using listen(), third step.
        soc.listen()
        # waiting for a connection from client and holding the address of client into the tuple./ fourth step
        connection, address = soc.accept()

        with connection:
            print("Connected by {}".format(address))

            while True:
                # recieve client data 
                data = connection.recv(1024)
                # if returns emty data then stop the loop
                if not data:
                    break
                # get data client send and return data
                connection.sendall(data)

# start function
server_connection()

