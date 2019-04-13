class Meta(type):
    """
    Наслідуємо від метакласу type
    для створення свого метакласу
    """
    def __new__(cls, name, parents, attrs):
        print(f'Creating {name}')

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)

    def __init__(cls, name, bases, attrs):
        print(f'Inicializing — {name}')

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


class Base(metaclass=Meta):
    pass


class A(Base):
    pass


class B(Base):
    pass


print(f'A.class_id: {A.class_id}\n')
print(Base.registry,
      Base.__subclasses__(),
      sep='\n')
