#functions for our bookbot project
#stats.py
def get_num_words(book_content):
    words = book_content.split()
    num_words = len(words)
    return num_words

def get_char_num(book_content):
    chars = {}
    lowered_words = book_content.lower()
    for char in lowered_words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars