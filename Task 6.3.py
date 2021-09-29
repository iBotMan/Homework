# Task 4.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.

# Repeats of letters in the word are removed, then the cipher alphabet is generated
# with the keyword matching to A, B, C etc. until the keyword is used up, whereupon
# the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# Encryption:
# Keyword is "Crypto"

# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z

# Example:

# cipher = Cipher("crypto")
# cipher.encode("Hello world")
# "Btggj vjmgp"

# cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
from string import ascii_uppercase, ascii_lowercase


class Cipher:
    __keyword = None
    __alphabet = ascii_uppercase + ascii_lowercase
    __cipher_alphabet = ascii_uppercase+ascii_lowercase
    __encode_table = dict()
    __decode_table = dict()

    def __init__(self, keyword=None):
        if keyword:
            self.__keyword = keyword
            self.__create_cipher_alphabet()
        self.__create_translation_tables()

    def __str__(self):
        return f'{self.__class__}'

    def __create_cipher_alphabet(self):
        alphabet_set = set(ascii_uppercase)
        keyword_set = set(self.__keyword.upper())
        difference = alphabet_set.difference(keyword_set)

        res = ''
        for x in self.__keyword.upper():
            if x not in res:
                res += x
        self.__cipher_alphabet = res.upper() + ''.join(sorted(difference))
        self.__cipher_alphabet = self.__cipher_alphabet+self.__cipher_alphabet.lower()

    def __create_translation_tables(self):
        for ind, item in enumerate(self.__alphabet):
            self.__encode_table[ord(item)]=ord(self.__cipher_alphabet[ind])
        for ind, item in enumerate(self.__cipher_alphabet):
            self.__decode_table[ord(item)]=ord(self.__alphabet[ind])

    def encode(self, string):
        return string.translate(self.__encode_table)

    def decode(self, string):
        return string.translate(self.__decode_table)


def main():
    cipher = Cipher("crypto")
    res = cipher.encode("Hello world")
    print(res)
    print(cipher.decode(res))


if __name__ == '__main__':
    main()


