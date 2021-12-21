import socket
import threading

LOCALHOST = "127.0.0.1"
PORT = 1488

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Сервер запущен!")


class ClientThread(threading.Thread):

    def __init__(self, client_address, client_socket) -> None:
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print(f"новое подключение: {client_address}")

    def run(self) -> None:
        msg = ""
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)

while True:
    server.listen(1)
    client_sock, client_address = server.accept()
    new_thread = ClientThread(client_address, client_sock)
    new_thread.start()

