import socket
import time


class ClientError(Exception):
    pass


class Client:
    """docstring for Client"""

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = int(port)
        self._timeout = int(timeout)

    def _send(self, cmd):
        with socket.create_connection((self._host, self._port),
                                      self._timeout) as sock:
            sock.sendall(cmd.encode("utf8"))
            data = sock.recv(1024)
            return data.decode('utf-8')

    def put(self, key, value, timestamp=None):
        """Зберігаємо метрики на сервері"""
        timestamp = timestamp or int(time.time())
        try:
            response = self._send(f"put {key} {value} {timestamp}\n")
            if response[0:3] != 'ok\n':
                raise ClientError(response)
        except socket.error as err:
            raise ClientError("Can't send data", err)

    def get(self, key):
        """отримуємо метрики"""
        response = self._send(f"get {key}\n")
        if response[0:3] != 'ok\n':
            raise ClientError(response)

        data = dict()
        lines = response.split('\n')
        for l in lines[1:-2]:
            metric = l.split(' ')
            res_key = metric[0]
            res_val = float(metric[1])
            res_ts = int(metric[2])
            if res_key not in data:
                data[res_key] = list()
            data[res_key].append((res_ts, res_val))
            data[res_key].sort(key=lambda tup: tup[0])

        return data


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
