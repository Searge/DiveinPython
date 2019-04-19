# Виклики корутин, PEP 380
def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_python_coroutine():
    g = grep("python")
    yield from g


if __name__ == '__main__':
    g = grep_python_coroutine()  # is g coroutine?

    g.send(None)
    g.send("python wow!")
    g.close()
