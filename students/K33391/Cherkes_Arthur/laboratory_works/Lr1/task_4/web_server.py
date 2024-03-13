import socket
import threading

HOST = '127.0.0.1'
PORT = 9093

cl_nick_socket = {}


def handle_client(cl_socket):
    nickname = cl_socket.recv(1024).decode("utf-8")
    cl_socket.send(f"Hello, {nickname}".encode("utf-8"))
    cl_nick_socket[nickname] = cl_socket

    while True:
        message = cl_socket.recv(1024).decode("utf-8")
        if not message:
            del cl_nick_socket[nickname]
            break
        for name, cl_tmp_socket in cl_nick_socket.items():
            cl_tmp_socket.send(f"{name}: {message}".encode("utf-8"))
    cl_socket.close()

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen()

while True:
    cl_socket, cl_addr = conn.accept()
    cl_thread = threading.Thread(target=handle_client, args=(cl_socket,))
    cl_thread.start()
