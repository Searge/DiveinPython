"""
ТЕСТОВЕ ЗАВДАННЯ
Створити інтерфейс для роботи з файлами.
Клас File має підтримувати кілька незвичних операцій
"""

from os import path
from tempfile import gettempdir


class File:
    """Файл з магічними методами :crystal_ball:"""

    def __init__(self, filename):
        self.filename = filename

        if not path.exists(self.filename):
            open(self.filename, 'w').close()

    def __str__(self):
        return self.filename

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, content):
        with open(self.filename, 'w') as f:
            return f.write(content)

    def __add__(self, obj):
        tmp = path.join(gettempdir(), self.filename)
        # 'str' object has no attribute 'write'
        # тому змінюємо тип:
        new_file = type(self)(tmp)
        new_file.write(self.read() + obj.read())

        return new_file

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        with open(self.filename, 'r') as f:
            f.seek(self._index)

            line = f.readline()
            if not line:
                self._index = 0
                raise StopIteration('End of File')

            self._index = f.tell()
            # Strip superfluous newline symbol
            return line.rstrip('\n')


def _main():
    first = File('first')
    second = File('second')
    new_obj = first + second

    print(f"Lines of {new_obj}:\n")
    for line in new_obj:
        print(line)


if __name__ == '__main__':
    _main()
