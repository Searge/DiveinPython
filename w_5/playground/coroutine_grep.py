# Сопрограммы (корутины)
def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


if __name__ == '__main__':
    g = grep("python")
    next(g)
    g.send("golang is better?")
    g.send("python is simple!")
