import os

with open("data.txt") as f:
    spam = f.readline()

    if os.fork() == 0:
        # Дочерній процес
        spam = f.readline()
        print("child:", spam)
    else:
        # Батьківський процес
        spam = f.readline()
        print('parent:', spam)
        os.wait()
