class FileReader:
    """docstring for FileReader"""
    def __init__(self, arg):
        self.arg = arg


reader = FileReader("example.txt")
print(reader.read())
