# Неблокуючий ввід/вивід
import socket
import select
sock = socket.socket()
sock.bind(("", 10001))
sock.listen()
# як обробити запити для conn1 і conn2
# одночасно без потоків?
conn1, addr = sock.accept()
conn2, addr = sock.accept()
conn1.setblocking(0)
conn2.setblocking(0)
epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)
conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2
}

# Цикл обробки подій в epoll
while True:
    events = epoll.poll(1)
    for fileno, event in events:
        if event & select.EPOLLIN:
            # обработка чтения из сокета
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            # обработка записи в сокет
            conn_map[fileno].send("pong".encode("utf8"))
