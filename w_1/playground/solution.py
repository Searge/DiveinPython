import sys
digit_string = sys.argv[1]


def calculate(string):
    result = 0
    for i in string:
        result += int(i)

    return(result)


if __name__ == '__main__':
    print(calculate(digit_string))
