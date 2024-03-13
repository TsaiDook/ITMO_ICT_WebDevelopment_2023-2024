import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9093))

discipline = input('Введите предмет: ')
grade = input('Введите отметку: ')

body = f"Content-Disposition: form-data; name=\"discipline\"\r\n\r\n{discipline}\r\n"
body += f"Content-Disposition: form-data; name=\"grade\"\r\n\r\n{grade}\r\n"

# Создаем POST-запрос с правильным форматом и контентом
request = f"POST / HTTP/1.1\r\nHost: localhost\r\nContent-Type: multipart/form-data\r\nContent-Length: {len(body)}\r\n\r\n{body}"


# Создаем POST-запрос с правильным форматом и контентом
request = f"POST / HTTP/1.1\nHost: localhost\nContent-Type: application/x-www-form-urlencoded\nContent-Length: {len(body)}\n\n{body}"

sock.send(request.encode())

response = sock.recv(2*1024).decode()
print(response)

sock.close()
