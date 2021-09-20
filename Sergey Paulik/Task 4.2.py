### Task 4.2
#Write a function that check whether a string is a palindrome or not. Usage of
#any reversing functions is prohibited. To check your implementation you can use
#strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).


def is_palindrome(input_data):
    input_data = str(input_data)
    new = ''.join(ch for ch in input_data.lower() if ch.isalnum())
    return (new[::-1] == new)


def main():
    input_data = 2002
    print(is_palindrome(input_data))

    input_data = 'Лёша на полке клопа нашёл'
    print(is_palindrome(input_data))

    input_data = 'redivider'
    print(is_palindrome(input_data))

    input_data = 'Do geese see God'
    print(is_palindrome(input_data))


if __name__ == '__main__':
    main()
