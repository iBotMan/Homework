"""
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:
```
Input: (1, 2, 3, 4)
Output: 1234
```
"""


def main():
    tuple_of_integers = (1, 2, 3, 4)
    number = int(''.join(map(str, tuple_of_integers)))
    print(number)


if __name__ == "__main__":
    main()

