### Task 4.10
#Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
#```python
#print(generate_squares(5))
#>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#```


def generate_squares(num):
    result = {}
    for i in range(1, num + 1):
        result[i] = i ** 2
    return result


if __name__ == '__main__':
    print(generate_squares(5))