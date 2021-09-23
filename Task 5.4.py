# Task 5.4
# Look through file `modules/legb.py`.
# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

a = "I am global variable!"


def enclosing_funcion_1():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    inner_function()


def enclosing_funcion_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        #a = "I am local variable!"

        print(a)

    inner_function()


def enclosing_funcion_3():
    a = "I am variable from enclosed function!"

    def inner_function():
        #a = "I am local variable!"
        print(a)

    inner_function()


if __name__ == '__main__':
    print(enclosing_funcion_1())
    print(enclosing_funcion_2())
    print(enclosing_funcion_3())





