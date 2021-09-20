# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.


def custom_replays(input_string, old, new):
    new = map(lambda item, d={ord(old): ord(new)}: chr(d[ord(item)]) if ord(item) in d else item, input_string)
    return (''.join(new))


def main():
    input_string = "\"asdfdfdf\"sdsdsa\'ss\" \'"
    print(custom_replays(input_string, '\'', "\""))
    print(custom_replays(input_string, '\"', "\'"))


if __name__ == '__main__':
    main()

