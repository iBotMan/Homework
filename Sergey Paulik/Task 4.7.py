### Task 4.7
#Implement a function `foo(List[int]) -> List[int]` which, given a list of
#integers, return a new list such that each element at index `i` of the new list
#is the product of all the numbers in the original array except the one at `i`.
#Example:
#```python
#>>> foo([1, 2, 3, 4, 5])
#[120, 60, 40, 30, 24]

#>>> foo([3, 2, 1])
#[2, 3, 6]
#```


def foo(input_list):
    max_product = 1
    for x in input_list:
        max_product *= x

    result = []
    for x in input_list:
        result.append(int(max_product / x))
    print(result)


if __name__ == '__main__':
    foo([1, 2, 3, 4, 5])
    foo([3, 2, 1])


