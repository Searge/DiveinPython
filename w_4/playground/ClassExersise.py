import random


class NoisyInt:
    """
    Додаємо рандомного шуму до операції додавання.
    """

    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        noise = random.uniform(-1, 1)
        return self.value + obj.value + noise


class PascalList:
    """
    Контейнер, який повертає число в списку по індексу, починаючи з 1, а не 0
    """

    def __init__(self, original_list=None):
        self.container = original_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()


if __name__ == '__main__':
    a = NoisyInt(10)
    b = NoisyInt(20)
    for i in range(3):
        print(a + b)
    numbers = PascalList(list(range(1, 6)))
    print('[1]:{}, [5]:{}'.format(numbers[1], numbers[5]))
