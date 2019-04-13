class Property:
    """Свій особистий клас Property"""

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        return self.getter(obj)


class Class:
    """Тестуємо створений декоратор разом зі стандартним @property"""
    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'

    custom_pure = Property(custom_pure)


obj = Class()

print(
    'obj.original\t\t' + obj.original,
    'obj.custom_pure\t\t' + obj.custom_pure,
    'obj.custom_sugar\t' + obj.custom_sugar,
    sep='\n'
)

print('Class.custom_sugar\t', Class.custom_sugar)
# ВИКЛИКАЄМО ЗБЕРЕЖЕНУ Ф_ЦІЮ
print('Property.__get__\t', Property.__get__)
