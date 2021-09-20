### Task 4.3
#Implement a function which works the same as `str.split` method
#(without using `str.split` itself, ofcourse).


def custom_split(string, sep=' '):
    result = []
    start = 0
    if sep in string:
        while True:
            fnd = string.find(sep, start)
            if fnd == -1:
                result.append(string[start:])
                break
            result.append(string[start:fnd])
            start = fnd + 1
    return result


def main():
    print(custom_split('sdsd -sdsdsd - ssss- ss','-'))


if __name__ == '__main__':
    main()



