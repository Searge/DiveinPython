import sys


class FileReader:
    """Changed in version 3.3: EnvironmentError, IOError, WindowsError,
    socket.error, select.error and mmap.error have been merged into OSError,
    and the constructor may return a subclass.
    """

    def __init__(self, filename):
        self.read_file = filename

    def read(self):
        try:
            with open(self.read_file) as f:
                return f.read()
        except OSError:
            print(OSError.errno, OSError.strerror)


def _main():
    filename = sys.argv[1]
    reader = FileReader(filename)
    print(reader.read())


if __name__ == '__main__':
    _main()
