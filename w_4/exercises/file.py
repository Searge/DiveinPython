"""
ТЕСТОВЕ ЗАВДАННЯ
Створити інтерфейс для роботи з файлами.
Клас File має підтримувати кілька незвичних операцій
"""

from os.path import exists


class File:
    """docstring for File"""

    def __init__(self, path):
        self.path = path

        if not exists(self.path):
            open(self.path, 'w').close()


