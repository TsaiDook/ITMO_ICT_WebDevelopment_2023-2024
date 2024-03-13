import socket
HOST = '127.0.0.1'
PORT = 9093
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

for i in range(3):
    data = conn.recv(1024)
    print(data.decode("utf-8"))
    param = str(input()).encode("utf-8")
    conn.send(param)
data = conn.recv(1024).decode("utf-8")
print(data)