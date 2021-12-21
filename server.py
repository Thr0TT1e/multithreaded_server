import socket
import threading

# Настройки сервера
LOCALHOST = "127.0.0.1"
PORT = 1488

# Разворачивает сервер по каналу TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Сервер запущен!")


# Поток для клиентов
class ClientThread(threading.Thread):

    # Инициализируем новое подключение
    def __init__(self, client_address, client_socket) -> None:
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print(f"Новое подключение: {client_address}")

    # Обработка полученных сообщений клиента
    def run(self) -> None:
        msg = ""
        while True:
            # Принимаем сообщение отправленных Байтов/Чанков
            data = self.csocket.recv(4096)
            # Декодируем Чанки в сообщение
            msg = data.decode()
            print(msg)

            # Если клиент отключился рвём соединение/выходим из цикла
            if msg == "":
                print("Отключение")
                break
            # обработка входящих сообщений
            elif msg == "дай денег":
                self.csocket.send(bytes("Денег нет, но Вы держитесь!", "UTF-8"))


# Запуск сервера в режиме прослушки
while True:
    server.listen(1)
    # При подключении Клиента обязательно принимаем соединение
    client_sock, client_address = server.accept()
    # Создаём отдельный поток для клиента в классе ClientThread
    new_thread = ClientThread(client_address, client_sock)
    new_thread.start()
