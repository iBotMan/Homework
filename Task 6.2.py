# Task 4.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
# After your own implementation of the class have a look at collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque


def set_history(function):
    def wrapper(*args, **kwargs):
        obj, key = args[0], args[1]
        result = function(*args)
        obj.get_history().append(key)
        if len(obj.get_history()) > 10:
            obj.get_history().pop(0)
        return result
    return wrapper


class HistoryDict(dict):

    def __init__(self, seq=None, **kwargs):
        super(HistoryDict, self).__init__(seq, **kwargs)
        self.__cash = []

    @set_history
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    @set_history
    def pop(self, key):
        return super().pop(key)

    def set_value(self, key, value):
        return self.__setitem__(key, value)

    def get_history(self):
        return self.__cash


d = HistoryDict({"foo": 42})
d["11"] = 11
d["12"] = 12
d["13"] = 13
d.set_value("bar", 43)
print(f'dict: {d}')
print(f'History: {d.get_history()}')


