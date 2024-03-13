import socket
HOST = '127.0.0.1'
PORT = 9093
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen()


def handle_request(client_socket):
    request = cl_socket.recv(1024).decode("utf-8")
    if request.startswith('GET / HTTP'):
        send_html(client_socket)


def send_html(client_socket):
    with open("index.html", "r") as file:
        response = 'HTTP/1.1 200 OK\n\n'
        response += file.read()
        client_socket.send(response.encode("utf-8"))


while True:
    cl_socket, cl_addr = conn.accept()
    handle_request(cl_socket)
