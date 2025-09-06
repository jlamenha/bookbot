from stats import countwords, countchars, report
import sys

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filedir = sys.argv[1]
    book_text = get_book_text(filedir)
    words = countwords(book_text)

    chars = countchars(book_text)

    report(chars, words, filedir)

def get_book_text(file_location):
    with open(file_location) as f:
        file_contents = f.read()
    return file_contents

main()