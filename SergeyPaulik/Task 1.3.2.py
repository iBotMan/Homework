"""
Create a program that asks the user for a number and then prints out a list of all the [divisors]
(https://en.wikipedia.org/wiki/Divisor) of that number.
Examples:
```
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
```
"""


def main():
    input_number = 60
    divisors = list()
    max_range = round(input_number**0.5)
    for x in range(1, max_range):
        if input_number % x == 0:
            divisors.append(x)
            divisors.append(input_number // x)
    print(sorted(divisors))


if __name__ == "__main__":
    main()
