### Task 7.10
# Implement a generator which will generate odd numbers endlessly.
# Example:
# ```python
# gen = endless_generator()
# while True:
# print(next(gen))
# >>> 1 3 5 7 ... 128736187263 128736187265 ...
# ```


def my_generator():
    result = 1
    while True:
        yield result
        result += 2


if __name__ == "__main__":
    generator = my_generator()
    while True:
        print(next(generator))