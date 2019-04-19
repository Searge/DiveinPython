class MyRangeIterator:
    def __init__(self, top):
        self.top = top
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.top:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


if __name__ == '__main__':
    counter = MyRangeIterator(3)
    print(counter)
    for it in counter:
        print(it)
"""
<__main__.MyRangeIterator object at 0x10d4cf208>
0
1
2
"""
