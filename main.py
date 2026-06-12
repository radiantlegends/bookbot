from stats import get_word_count, get_char_count, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def print_report(filepath, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_list:
        if d[0].isalpha():
            print(f"{d[0]}: {d[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    word_count = get_word_count(text)
    char_dict = get_char_count(text)
    sorted_list = chars_dict_to_sorted_list(char_dict)

    print_report(book, word_count, sorted_list)

main()