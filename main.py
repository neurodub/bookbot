f = ""
file_contents = "" 
book_content = ""
path_to_file = "./books/frankenstein.txt"
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        book_content = file_contents
    return book_content

def main():
    book_content = get_book_text(path_to_file)
    print(book_content)

main()
