# Task 7.4
# Implement decorator for supressing exceptions.
# If exception not occure write log to console.


def supressing_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            print(f'Exception - {exc} {type(exc)} in {func}')
    return wrapper


@supressing_exceptions
def func1(num):
    x = num / 0


def func2():
    y = 100


if __name__ == '__main__':
    func1(1)
    func2()
