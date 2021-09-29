# Task 4.8

# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.

#Example:
# pages = Pagination('Your beautiful text', 5)
# pages.page_count

# pages.item_count
# 19

# pages.count_items_on_page(0)
# 5
# pages.count_items_on_page(3)
# 4
# pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.

# Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
# If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

# Example:

# pages.find_page('Your')
# [0]
# pages.find_page('e')
# [1, 3]
# pages.find_page('beautiful')
# [1, 2]
# pages.find_page('great')
# Exception: 'great' is missing on the pages
# pages.display_page(0)
# 'Your '

from math import ceil


class Pagination:
    def __init__(self, txt, symbols):
        self.txt = txt
        self.symbols = symbols
        self.page_count = ceil(len(txt)/symbols)

    def find_page(self, word):
        start, result = 0, set()
        while True:
            find = self.txt.find(word, start)
            if find == -1: break
            result.add(find // self.symbols)
            result.add(((find - 1) + len(word)) // self.symbols)
            start = find + 1
        if len(result) == 0:
            raise Exception(f'"{word}" is missing on the pages')
        return list(result)

    def count_items_on_page(self, page):
        if not isinstance(page, int) or self.page_count <= page:
            raise Exception('Invalid index. Page is missing.')
        if page == (self.page_count-1):
            return len(self.txt) - page * self.symbols
        else:
            return self.symbols

    def display_page(self, page):
        if not isinstance(page, int) or self.page_count <= page:
            raise Exception('Invalid index. Page is missing.')
        return self.txt[self.symbols * page: self.symbols * (page + 1)]


def main():
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count)
    print(pages.find_page('Your'))
    # [0]
    print(pages.find_page('e'))
    # [1, 3]
    print(pages.find_page('beautiful'))
    # [1, 2]
    print(pages.count_items_on_page(3))
    #4
    print(pages.display_page(0))
    pages.find_page('great')


if __name__ == '__main__':
    main()

