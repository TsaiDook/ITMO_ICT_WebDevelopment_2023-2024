import socket
HOST = '127.0.0.1'
PORT = 9093
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen()


def find_solution(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return None
    elif disc == 0:
        return -b / 2 / a
    else:
        sqr_disc = disc ** (1 / 2)
        return (-b + sqr_disc) / 2 / a, (-b - sqr_disc) / 2 / a


while True:
    cl_socket, cl_addr = conn.accept()
    params = dict.fromkeys(["a", "b", "c"])
    for param in params:
        cl_socket.send(f"Введите параметр {param}".encode("utf-8"))
        data = cl_socket.recv(1024)
        params[param] = int(data.decode("utf-8"))
    res = find_solution(params["a"], params["b"], params["c"])

    msg = "Ответ: \n"
    if res:
        for x in res:
            msg += f"X = {x}\n"
    else:
        msg += "Корней нет"
    cl_socket.send(msg.encode("utf-8"))
