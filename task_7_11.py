# Task 7.11
# Implement a generator which will geterate [Fibonacci numbers]
# (https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
# Example:
# ```python
# gen = endless_fib_generator()
# while True:
# print(next(gen))
# >>> 1 1 2 3 5 8 13 ...
# ```

def fibonacci_numbers():
    fib1 = fib2 = 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


if __name__ == "__main__":
    f_b = fibonacci_numbers()
    while True:
        print( next(f_b) )