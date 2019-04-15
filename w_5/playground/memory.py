import os

spam = "eggs"

if os.fork() == 0:
    # Дочерній процес
    spam = "ham"
    print("child:", spam)
else:
    # Батьківський процес
    print('parent:', spam)
    os.wait()
