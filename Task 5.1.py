# Task 5.1

# Open file `data/unsorted_names.txt` in data folder.
# Sort the names and write them to a new file called `sorted_names.txt`.
# Each name should start with a new line as in the following example:

"""
Adele
Adrienne
...
Willodean
Xavier
"""


def main():

    with open('data/unsorted_names.txt', 'r') as unsorted_names_txt:
        sorted_names = tuple(sorted([name for name in unsorted_names_txt]))

    with open('data/sorted_names.txt', 'w') as sorted_names_txt:
        for name in sorted_names:
            sorted_names_txt.write(name)


if __name__ == '__main__':
    main()

