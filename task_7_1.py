### Task 7.1
# Implement class-based context manager for opening and working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.


class OpenFile:
    def __init__(self, filename: str, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exception, value, traceback):
        self.file.close()


if __name__ == '__main__':
    with OpenFile('my.txt', 'r') as file:
        result = file.read()
        print(result)
        