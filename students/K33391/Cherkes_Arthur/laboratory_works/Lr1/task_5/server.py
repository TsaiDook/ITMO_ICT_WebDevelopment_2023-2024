import socket
from collections import defaultdict

class MyHTTPServer:
    def __init__(self, ip, port):

        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.conn.bind((host, port))
        self.conn.listen(5)

        self.grades = defaultdict(list)

    # Старт сервера
    def serve_forever(self):
        while True:
            client, addr = self.conn.accept()
            self.serve_client(client)

    # Прослушивание клиента
    def serve_client(self, client):
        data = client.recv(2 * 16384).decode(encoding="utf-8", errors="ignore")
        self.parse_request(client, data)

    # Парсим запросы
    def parse_request(self, client, data):
        lines = data.split("\n")
        method, url, version = lines[0].split()

        if method == "GET":
            params = (
                {p.split("=")[0]:p.split("=")[1] for p in url.split("?")[1].split("&")}
                if "?" in url
                else None
            )

        elif method == "POST":
            discipline = None
            grade = None

            for line in lines:
                if 'Content-Disposition: form-data; name="discipline"' in line:
                    discipline = lines[lines.index(line) + 2].strip()
                elif 'Content-Disposition: form-data; name="grade"' in line:
                    grade = lines[lines.index(line) + 2].strip()

            params = {"discipline": discipline, "grade": grade}

        else:
            params = None

        self.handle_request(client, method, params)

    # Обработка  запросов
    def handle_request(self, client, method, params):
        if method == "GET":
            self.send_response(client, 200, "OK", self.generate_html())
            print("GET 200 OK")
        elif method == "POST":
            discipline = params.get("discipline")
            grade = params.get("grade")
            self.grades[discipline].append(grade)


            self.send_response(client, 200, "OK", f'{discipline}: {grade} добавлено')
            print("POST 200 OK")
        else:
            self.send_response(client, 404, "Not Found")
            print("ERR  404")

    # Отправка ответа
    def send_response(self, client, code, reason, body):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    # Генерация HTML
    def generate_html(self):
        page = (
            "<html><body><div>"
            f"{''.join([f'<p>{discipline}: {grade}</p>' for discipline, grade in self.grades.items()])}"
            "</div></body></html>"
        )
        return page

if __name__ == "__main__":
    host = "localhost"
    port = 9093
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.conn.close()