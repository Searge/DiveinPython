# Синхронізація потоків, блокувальники
import threading


class Point(object):
    def __init__(self, x, y):
        self.mutex = threading.RLock()
        self.set(x, y)

    def get(self):
        with self.mutex:
            return (self.x, self.y)

    def set(self, x, y):
        with self.mutex:
            self.x = x
            self.y = y


# use in threads
my_point = Point(10, 20)
my_point.set(15, 10)
my_point.get()
