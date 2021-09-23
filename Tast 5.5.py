# Task 5.5
# Implement a decorator `remember_result` which remembers last result of function it decorates
# and prints it before next call.

last_result = None


def remember_result(func):
	def wrapper(*args):
		global last_result
		print(f"Last result = '{last_result}'")
		last_result = func(*args)
		return func
	return wrapper


@remember_result
def sum_list(*args):
	result = ''
	if isinstance(args[0], int):
		result = 0

	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result


if __name__ == '__main__':
	sum_list("a", "b")
	sum_list("abc", "cde")
	sum_list(3, 4, 5)