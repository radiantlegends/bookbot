def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_count(item):
    return item["count"]

def sorted_char_count(chars_dict):
    sorted_list = []
    for char in chars_dict:
        current_char = {"char": char, "count": chars_dict[char]}
        sorted_list.append(current_char)
    sorted_list.sort(key=get_count, reverse=True)
    return sorted_list