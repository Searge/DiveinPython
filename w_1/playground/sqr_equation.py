import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def quad_equat(a, b, c):
    D = (abs(b) ** 2 - (4 * a * c)) ** 0.5
    x1 = (abs(b) - D) / (2 * a)
    x2 = (abs(b) + D) / (2 * a)
    print(int(x1))
    print(int(x2))


quad_equat(a, b, c)
