# Task 7.2
# Implement context manager for opening and working with file,
# including handling exceptions with @contextmanager decorator.

from contextlib import contextmanager


@contextmanager
def file_open(file_path, mode='r'):
    try:
        file_obj = open(file_path, mode, encoding='utf-8')
        yield file_obj  # return
    except Exception as e:
        print(f"Error - {e} {type(e)}")
    finally:
        print('Closing file')
        file_obj.close()


if __name__ == '__main__':
    with file_open('file.txt', 'w') as file:
        print(f'Resource = {file}')
        raise Exception('SomeError')