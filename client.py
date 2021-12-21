import socket
from threading import Thread
import threading

# Прописываем настройки сервера
SERVER = "127.0.0.1"
PORT = 1488

# Настройка связи с сервером по TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Thr0TT1e", "UTF-8"))


# Слушаем сервер
def task() -> None:
    while True:
        in_data = client.recv(4096)
        print(f"От сервера: {in_data.decode()}")


# Ввод и отправка сообщения пользователя на сервер
def send_message() -> None:
    while True:
        out_data = input("Введите сообщение: ")
        client.sendall(bytes(out_data, "UTF-8"))
        print(f"Отправлено: {str(out_data)}")


# Помещаем функции в отдельные потоки
t1 = Thread(target=send_message)
t2 = Thread(target=task)

# Запускаем потоки
t1.start()
t2.start()

t1.join()
t2.join()
