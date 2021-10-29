# Task 7.8
# Implement your custom iterator class called MySquareIterator
# which gives squares of elements of collection it iterates through.
# Example:
# ```python
# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25

class MySquareIterator:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        res = self.data[self.index] ** 2
        self.index += 1
        return res


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)
    for item in itr:
        print(item)