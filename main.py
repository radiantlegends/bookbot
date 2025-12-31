from stats import get_word_count, get_char_count, sorted_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_list = sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at", book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['count']}")
    print("============= END ===============")

main()