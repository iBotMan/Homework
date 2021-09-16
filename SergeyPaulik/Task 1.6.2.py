"""
Write a program which makes a pretty print of a part of the multiplication table.
Examples:
```
Input:
a = 2
b = 4
c = 3
d = 7
Output:
    3	4	5	6	7
2	6	8	10	12	14
3	9	12	15	18	21
4	12	16	20	24	28
```
"""


def main():

    # rows
    a = 2
    b = 4
    # columns
    c = 3
    d = 7

    print(end="\t")
    for column in range(c, d+1):
        print(column, end="\t")
    print()
    for row in range(a, b+1):
        print(row, end="\t")
        for column in range(c, d+1):
            print(row * column, end="\t")
        print()


if __name__ == '__main__':
    main()

