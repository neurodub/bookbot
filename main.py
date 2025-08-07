from stats import get_num_words
from stats import get_char_num
path_to_file = "./books/frankenstein.txt"
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        book_content = file_contents
    return book_content

def main():
    book_content = get_book_text(path_to_file)
    num_words_output = get_num_words(book_content)
    # print(book_content)
    print(f"{num_words_output} words found in the document")
    chars = get_char_num(book_content)
    print(chars)

main()
