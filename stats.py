def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text: str) -> dict[str, int]:
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_count(item):
    return item["count"]

def sort_on(book: tuple[str, int]) -> int:
    return book[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []
    for k, v in chars_dict.items():
        new_tuple = (k, v)
        new_list.append(new_tuple)
    return sorted(new_list, key=sort_on, reverse=True)