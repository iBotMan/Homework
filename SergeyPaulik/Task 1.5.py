"""
Write a Python program to print all unique values of all dictionaries in a list.
Examples:
```
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
```
"""


def main():
    list_of_dicts = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    all_unique_values = set()

    for dict_from_list in list_of_dicts:
        all_unique_values.add(list(dict_from_list.values())[0])
    print(all_unique_values)


if __name__ == "__main__":
    main()

