from os import path, remove
from tempfile import gettempdir
from argparse import ArgumentParser
from json import loads, dumps


storage_path = path.join(gettempdir(), 'storage.data')


def get_data():
    if not path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return loads(raw_data)
        # Повертаємо пустий словник
        return {}


def put(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(dumps(data))


def get(key):
    data = get_data()

    return data.get(key)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='Clear')

    parser.add_argument('-k', '--key', help='Key')
    parser.add_argument('-v', '--val', help='Value')

    args = parser.parse_args()

    if args.clear:
        remove(storage_path)
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')
