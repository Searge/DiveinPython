class Meta:
    """
    Наслідуємо від метакласу type
    для створення свого метакласу
    """
    def __new__(cls, name, parents, attrs):
        print(f'Creating {name}')

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass


print(f'A.class_id: {A.class_id}')
