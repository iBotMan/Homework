"""
Write a Python program to sort a dictionary by key.
Examples:
```
Input: {"b": 9, 10: 10, 9: 9, "c": 7, "a": "7", False: 7}
```
"""


def main_1():

    unsorted_dict_any_type_key = {"w": 1, "b": 9, 10: 232, 9: 1, "a": "4", True: 1, False: 99}

    dict_of_types = {}
    for key in unsorted_dict_any_type_key.keys():
        type_of_key = type(key)
        val = dict_of_types.get(type_of_key, list())
        val.append(key)
        dict_of_types[type_of_key] = val

    sorted_dict = {}
    for list_of_keys in dict_of_types.values():
        for key in sorted(list_of_keys):
            sorted_dict[key] = unsorted_dict_any_type_key[key]

    print("main_1: ", end="\t")
    print(sorted_dict)


def main_2():
    unsorted_dict_string_key = {"w": 1, "b": 9, "10": 232, "9": 1, "a": "4"}
    sorted_dict = {}
    for key in sorted(unsorted_dict_string_key):
        sorted_dict[key] = unsorted_dict_string_key[key]
    print("main_2: ", end="\t")
    print(sorted_dict)


def main_3():
    unsorted_dict_any_type_key = {"w": 1, "b": 9, 10: 232, 9: 1, "a": "4", True: 1, False: 99}

    unsorted_dict_string_key = {}
    sorted_dict = {}
    for key in unsorted_dict_any_type_key:
        unsorted_dict_string_key[str(key)] = unsorted_dict_any_type_key[key]

    for key in sorted(unsorted_dict_string_key):
        sorted_dict[key] = unsorted_dict_string_key[key]

    print("main_3: ", end="\t")
    print(sorted_dict)


if __name__ == "__main__":
    main_1()
    main_2()
    main_3()

