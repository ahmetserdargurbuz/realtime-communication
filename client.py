import socket
import sys
import util

server_address = (sys.argv[1], int(sys.argv[2]))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Start Receiving
util.start_receiving(client_socket)

# Write thread
util.start_writing(client_socket)

# Close socket
client_socket.close()
