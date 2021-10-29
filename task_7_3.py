# Task 7.3
# Implement decorator with context manager support for
# writing execution time to log-file. See contextlib module.

import time
from contextlib import ContextDecorator


class writing_execution_time(ContextDecorator):

    def __init__(self, path: str, mode='a'):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.start_time = time.perf_counter()
        self.file = open(self.path, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exception, value, traceback):
        self.stop_time = time.perf_counter()
        self.file.write(f'{self.stop_time - self.start_time} sec\n')
        self.file.close()


@writing_execution_time('log.txt')
def func1(num):
    return [i for i in range(num)]


@writing_execution_time('log.txt')
def func3(num):
    return [i + 1 for i in range(num)]


@writing_execution_time('log.txt')
def func2(num):
    list = []
    for i in range(num):
        list.append(i)
    return list


if __name__ == "__main__":
    func1(5)
    print(func1(5))
    func2(5)
    func3(5)