# asyncio, Hello World
import asyncio


@asyncio.coroutine
def hello_world():
    while True:
        print("Hello World!")
        yield from asyncio.sleep(1.0)


if __name__ == '__main__':
    # отримуємо цикл обробки подій
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())
    # закриваємо роботу з циклом подій
    loop.close()
