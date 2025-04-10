import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_on
from stats import report_char_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    # book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    char_dict = get_char_count(file_contents)
    char_count_list = report_char_count(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_count_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()