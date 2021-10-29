# Task 7.9
# Implement an iterator class EvenRange, which accepts start
# and end of the interval as an init arguments and gives only even numbers during iteration.
# If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
# _Note: Do not use function `range()` at all_
# Example:
# ```python
# er1 = EvenRange(7,11)
# next(er1)
# >>> 8
# next(er1)
# >>> 10
# next(er1)
# >>> "Out of numbers!"
# next(er1)
# >>> "Out of numbers!"
# er2 = EvenRange(3, 14)
# for number in er2:
#     print(number)
# >>> 4 6 8 10 12 "Out of numbers!"
# ```


class EvenRange:

    def __init__(self, start, end):
        if EvenRange.is_even_num(start):
            self.start = start
        else:
            self.start = start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            print('Out of numbers!')
            raise StopIteration
        res = self.start
        self.start += 2
        return res

    @staticmethod
    def is_even_num(num):
        if num % 2 != 0:
            return False
        return True


if __name__ == "__main__":
    result_1 = EvenRange(7, 11)

    print(next(result_1))
    print(next(result_1))
    print(next(result_1))

    result_2 = EvenRange(3, 14)
    for number in result_2:
        print(number, end=" ")