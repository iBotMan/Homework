"""
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in
sorted form.
Examples:
```
Input: red,white,black,red,green,black
Output: ["black", "green", "red", "white"]
```
"""


def main():
    string = "red,white,black,red,green,black"
    data = string.split(",")
    sorted_form = sorted(list(set(data)))
    print(sorted_form)


if __name__ == "__main__":
    main()

