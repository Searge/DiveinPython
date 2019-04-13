def dummy_factory():
    class Class:
        pass
    return Class


Dummy = dummy_factory()

print(Dummy() is Dummy())


# Створення класу одним рядком:
NewClass = type('NewClass', (), {})
print(
    NewClass,
    NewClass(),
    sep='\n'
)
