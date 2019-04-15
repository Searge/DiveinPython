import os
import time

pid = os.fork()
if pid == 0:
    # Дочерній процес
    while True:
        print('child:', os.getpid())
        time.sleep(5)
else:
    # Батьківський процес
    print('parent:', os.getpid())
    os.wait()
