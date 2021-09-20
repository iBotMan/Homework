### Task 4.9
#Implement a bunch of functions which receive a changeable number of strings and return next parameters:

#1) characters that appear in all strings

#2) characters that appear in at least one string

#3) characters that appear at least in two strings

#4) characters of alphabet, that were not used in any string

#Note: use `string.ascii_lowercase` for list of alphabet letters

#```python
#test_strings = ["hello", "world", "python", ]
#print(test_1_1(*strings))
#>>> {'o'}
#print(test_1_2(*strings))
#>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
#print(test_1_3(*strings))
#>>> {'h', 'l', 'o'}
#print(test_1_4(*strings))
#>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
#```

from string import ascii_lowercase


def my_function(input_list, quantity):
    if quantity == 0:
        return set(ascii_lowercase).difference(*input_list)

    if quantity == len(input_list):
        return set(ascii_lowercase).intersection(*input_list)

    count_dict = {}
    unq = ''
    for _, item in enumerate(input_list):
        unq += ''.join(str(ch) for ch in set(item))

    for ch in unq:
        if unq.count(ch) >= quantity:
            count_dict[ch] = unq.count(ch)

    return set(count_dict.keys())


def test_1_1(*test_list):
    return my_function(test_strings, len(test_list))


def test_1_2(*test_list):
    result = my_function(test_list, 1)
    return result


def test_1_3(*test_list):
    result = my_function(test_list, 2)
    return result


def test_1_4(*test_list):
    result = my_function(test_list, 0)
    return result


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]
    print('Test 1_1', end='\t')
    print(test_1_1(*test_strings))

    print('Test 1_2', end='\t')
    print(test_1_2(*test_strings))

    print('Test 1_3', end='\t')
    print(test_1_3(*test_strings))

    print('Test 1_4', end='\t')
    print(test_1_4(*test_strings))
