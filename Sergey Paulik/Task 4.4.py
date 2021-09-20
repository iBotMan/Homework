### Task 4.4
#Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
#which splits the `s` string by indexes specified in `indexes`. Wrong indexes
#must be ignored.
#Examples:
"""python
#>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
#["python", "is", "cool", ",", "isn't", "it?"]

#>>> split_by_index("no luck", [42])
#["no luck"]
"""


def split_by_index(input_string, indexes):
    indexes.append(len(input_string))
    start = 0
    result = []
    for ind in indexes:
        result.append(input_string[start:ind])
        start = ind

    return result


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))