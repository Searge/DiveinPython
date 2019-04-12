class Value:
    """docstring for Value"""

    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class Class:
    """docstring for Class"""
    attr = Value()


instance = Class()
instance.attr = 10
print(instance.attr)
