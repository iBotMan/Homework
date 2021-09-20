### Task 4.8
#Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
#of tuples containing pairs of elements. Pairs should be formed as in the
#example. If there is only one element in the list return `None` instead.
#Example:
#```python
#>>> get_pairs([1, 2, 3, 8, 9])
#[(1, 2), (2, 3), (3, 8), (8, 9)]

#>>> get_pairs(['need', 'to', 'sleep', 'more'])
#[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

#>>> get_pairs([1])
#None
#```


def get_pairs(input_list):
    if len(input_list) < 2:
        return None
    result = []
    #for x in range(len(input_list)-1):
        #result.append((input_list[x], input_list[x+1]))
    for x, _ in enumerate(input_list):
        if x < len(input_list)-1:
            result.append((input_list[x], input_list[x + 1]))

    print(result)


if __name__ == '__main__':
    get_pairs([1, 2, 3, 8, 9])
    get_pairs(['need', 'to', 'sleep', 'more'])
