import socket
HOST = '127.0.0.1'
PORT = 9093
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))


conn.send("Hello, Server".encode('utf-8'))
data = conn.recv(1024).decode('utf-8')
print(data)
conn.close()
