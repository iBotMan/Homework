# Task 7.6
# Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from
# Task 5.5 for validating input, handle all exceptions and print user friendly output.


import task_7_5


def input_data():
    input_num = int(input())
    return input_num


def counter_and_print_pairs(even_num: int):
    first_num = 2
    while True:
        if is_prime_num(first_num):
            second_num = even_num - first_num
            if is_prime_num(second_num):
                return print(f"{even_num} = {first_num} + {second_num}")
        first_num += 1


def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    while True:
        try:
            num = input_data()
            if task_7_5.is_num_even(num) == True:
                counter_and_print_pairs(num)
                close_session = input('Input "q" to quit or any key to continue: ')
                if close_session == 'q':
                    break

        except task_7_5.MyTypeError as exc_type:
            print(f'{exc_type}')
        except task_7_5.MyValueError as exc_value:
            print(f'{exc_value}')


if __name__ == '__main__':
    main()
