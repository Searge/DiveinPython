class Client:
    """docstring for Clien"""
    def __init__(self, arg):
        self.arg = arg

    def put():
        """Зберігаємо метрики на сервері"""
        pass

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
