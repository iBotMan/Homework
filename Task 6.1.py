# Task 4.1
# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."

# Implement to methods: "increment" and "get"

#If you are familiar with Exception rising use it to display the "Maximal value is reached


class Counter(object):
    __value = 0
    __stop = None

    def __init__(self, start=None, stop=None):
        if start:
            self.__value = start
        if stop:
            self.__stop = stop

    def increment(self):
        if self.__stop and self.__stop<self.__value+1:
            print('Maximal value is reached.')
        else:
            self.__value += 1

    def get(self):
        print(self.__value)


if __name__ == '__main__':
    c = Counter(start=42)
    c.increment()
    c.get()

    c = Counter()
    c.increment()
    c.get()

    c.increment()
    c.get()

    c = Counter(start=42, stop=43)
    c.increment()
    c.get()

    c.increment()
    c.get()