# Task 5.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

# python
# def most_common_words(filepath, number_of_words=3):
#   pass

# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.


from string import ascii_lowercase


def get_clear_string(string):
    dict_tr = {item: '' for item in set(string).difference(ascii_lowercase)}
    dict_tr.pop(' ', None)
    translation = string.maketrans(dict_tr)
    return string.translate(translation)


def get_clear_word(word):
    if not word[-1].isalnum():
        return word[:-1]
    return word


def most_common_words(file_path, number_of_words=3):

    count_of_words = {}

    with open('data/'+file_path, 'r') as lorem_ipsum_txt:
        for line in lorem_ipsum_txt:
            line = line * 9999
            #for word in get_clear_string(line.lower()).split():
            for word in line.lower().split():
                if not word[-1].isalnum():
                    count_of_words[word[:-1]] = count_of_words.get(word[:-1], 0) + 1
                else:
                    count_of_words[word] = count_of_words.get(word, 0) + 1

    sorted_count_of_words = sorted(count_of_words.items(), key=(lambda item: item[1]), reverse=True)
    return [sorted_count_of_words[i][0] for i in range(number_of_words)]


if __name__ == '__main__':
    print(most_common_words('lorem_ipsum.txt'))



