import socket
import time.time


class ClientError(Exception):
    pass


class Client:
    """docstring for Client"""

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = int(port)
        self._timeout = int(timeout)

        self._socket = socket.create_connection((host, self._port),
                                                self._timeout)

    def _read(self):
        """Читаємо відповіді сервера"""
        data = b""

        while not data.endswith(b"\n\n"):
            data += self._socket.recv(1024)

        status, payload = data.decode().split("\n", 1)

        return payload.strip()

    def put(self, key, value, timestamp=None):
        """Зберігаємо метрики на сервері"""
        timestamp = timestamp or int(time())
        self._socket.sendall(
            f"put {key} {value} {timestamp}\n".encode())

        self._read()

    def get():
        """отримуємо метрики"""
        pass


def _main():
    client = Client("127.0.0.1", 8888, timeout=15)

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("*"))


if __name__ == '__main__':
    _main()
