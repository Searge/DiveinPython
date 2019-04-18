# Створення сокету, контекстний менеджер
# клієнт
import socket

with socket.create_connection(("127.0.0.1", 10001)) as sock:
    sock.sendall("ping".encode("utf8"))
