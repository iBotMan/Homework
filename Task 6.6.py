# Task 6.6

# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.

# Example:

# p = Sun.inst()
# f = Sun.inst()
# p is f
# True


class Sun:
    __instance = None

    @classmethod
    def inst(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls, *args, **kwargs)
        return cls.__instance


def main():
    p = Sun().inst()
    f = Sun().inst()
    print(p is f)


if __name__ == '__main__':
    main()

