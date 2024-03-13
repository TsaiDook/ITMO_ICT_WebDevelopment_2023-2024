import socket
HOST = '127.0.0.1'
PORT = 9093
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen()


while True:
    cl_socket, cl_addr = conn.accept()
    data = cl_socket.recv(1024)
    udata = data.decode('utf-8')
    print(udata)

    msg = "Hello, Client".encode('utf-8')
    cl_socket.send(msg)

