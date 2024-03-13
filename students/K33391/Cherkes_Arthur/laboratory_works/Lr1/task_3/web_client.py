import socket
HOST = '127.0.0.1'
PORT = 9093
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

request = 'GET / HTTP/1.1\r\n\r\n'
conn.send(request.encode("utf-8"))
response = conn.recv(1024).decode("utf-8")
print(response)
conn.close()
