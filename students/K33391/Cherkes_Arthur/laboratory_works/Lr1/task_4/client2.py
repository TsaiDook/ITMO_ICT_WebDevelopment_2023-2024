import socket
import threading

HOST = '127.0.0.1'
PORT = 9093

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))


def receive_msg():
    while True:
        msg = conn.recv(1024).decode("utf-8")
        print(msg)


nickname = input("Write nickname\n")
conn.send(nickname.encode("utf-8"))

receive_thread = threading.Thread(target=receive_msg)
receive_thread.start()

while True:
    msg = input()
    conn.send(msg.encode("utf-8"))

