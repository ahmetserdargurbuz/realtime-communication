# realtime-communication

## Description:
This application is a demonstration of a server-client realtime communication using TCP.

server and client can both send and receive messages simultaneously in a non-blocking way. 

## Run:

python server.py [HOST] [PORT]

python client.py [SERVER_HOST] [SERVER_PORT] 

## Notes:

TCP may not send a whole message within a single packet. To demonstrate that the BUFFER_SIZE constant is intentionally set to a small number (8 bytes). Instead, the application uses an ENDLINE character as a termination signal. Thereby, the application displays the message to the user once it collects all the characters up to the ENDLINE character. 

Since client.py and server.py do almost the same job, to increase code reusability, I have written the functions in a single file (util.py). Also, the constants (ENDLINE, BUFFER_SIZE, SHUT_CMD) can be changed in that file. 

Getting input from the user and sending the message use the main thread. Receiving messages from the opponent uses another thread. 
