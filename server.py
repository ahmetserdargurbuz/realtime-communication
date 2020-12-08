import socket
import sys
import util

server_address = (sys.argv[1], int(sys.argv[2]))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

(client_socket, client_address) = server_socket.accept()
print(client_address, "co.")


# Welcome Client
util.send_msg(client_socket, "Hello Stranger! I am the server.")

# Start Receiving
util.start_receiving(client_socket)

# Write Thread
util.start_writing(client_socket)

# Close sockets
client_socket.close()
server_socket.close()
