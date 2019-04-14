class Value:
    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value - value * obj.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


def _main():
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)


if __name__ == '__main__':
    _main()
