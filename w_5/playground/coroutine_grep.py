# Співпрограма або співпроцедура (Coroutine)
"""
компонент програми, що узагальнює поняття підпрограми,
додатковою підтримкою безлічі точок входу (а не однієї, як підпрограма)
і зупинку та продовження виконання із збереженням певного положення.
"""


def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")


if __name__ == '__main__':
    g = grep("python")
    next(g)
    g.send("golang is better?")
    g.send("python is simple!")
    # Передаємо виключення в корутину:
    g.throw(RuntimeError, "something wrong")
    g.close()
