import threading

BUFFER = 8
ENDLINE = "#"
SHUT_CMD = "shut"


def send_msg(client_socket, msg):
    client_socket.send((msg+ENDLINE).encode("utf8"))


def print_msg(msg):
    print("=> " + msg)


def flush(full_msg):
    print_msg("".join(full_msg))
    full_msg.clear()


def stream_read(client_socket):
    full_msg = []
    while True:
        msg = client_socket.recv(BUFFER).decode('utf8')
        if not msg:  # Connection closed
            break

        start = 0
        for i in range(len(msg)):
            if msg[i] == ENDLINE:
                full_msg.append(msg[start: i])
                flush(full_msg)
                start = i+1
        full_msg.append(msg[start: len(msg)])


def start_receiving(client_socket):
    read_thread = threading.Thread(target=stream_read, args=(client_socket,))
    read_thread.setDaemon(True)
    read_thread.start()


def start_writing(client_socket):
    while True:
        msg = input()
        if msg == SHUT_CMD:
            break
        send_msg(client_socket, msg)
