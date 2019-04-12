class Descriptor:
    """docstring for Descrip"""

    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')


class Class:
    """docstring for Class"""
    attr = Descriptor()


instance = Class()
instance.attr

instance.attr = 10

del instance.attr
