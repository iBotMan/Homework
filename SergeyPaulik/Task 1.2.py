"""
Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
Examples:
```
Input: Oh, it is python
Output: {",": 1, " ": 3, "o": 2, "h": 2, "i": 2, "t": 2, "s": 1, "p": 1, "y": 1, "n": 1}
```
"""


def main():
    string = "Oh, it is python"
    dict_char = {}
    for character in string.lower():
        if character not in dict_char:
            dict_char[character] = 1
        else:
            dict_char[character] += 1
    print(dict_char)


if __name__ == "__main__":
    main()

