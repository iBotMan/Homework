"""
Write a Python program to calculate the length of a string without using the `len` function.
Examples:
```
Input: Oh, it is python
Output: 16
```
"""


def main():
    input_string = "Oh, it is python"
    string_len = input_string.rindex(input_string[-1]) + 1
    print(string_len)


if __name__ == "__main__":
    main()

