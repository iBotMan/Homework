### Task 4.6
#Implement a function `get_shortest_word(s: str) -> str` which returns the
#longest word in the given string. The word can contain any symbols except
#whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
#the string with a same length return the word that occures first.
#Example:
#```python
#>>> get_shortest_word('Python is simple and effective!')
#'effective!'

#>>> get_shortest_word('Any pythonista like namespaces a lot.')
#'pythonista'
#```


def get_shortest_word(input_string):
    print(max(input_string.split(), key=len))


if __name__ == '__main__':
    get_shortest_word('Python is simple and effective!')

    get_shortest_word('Any pythonista like namespaces a lot.')


