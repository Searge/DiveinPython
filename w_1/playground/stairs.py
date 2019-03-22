import sys
num_steps = sys.argv[1]
height = int(num_steps)

for step in range(1, height + 1):
    space = " " * (height - step)
    print(space + "#" * step)
