from functools import wraps
from json import dumps


def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return dumps(func(*args, **kwargs))

    return wrapper


@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data())
print(get_data.__name__)
