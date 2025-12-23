def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    
    for char in text:
        lower_char = char.lower()
        # Only count alphabetic characters
        if lower_char.isalpha():
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    
    return char_count

def convert_to_list(char_count):
    return [{"char": char, "num": count} for char, count in char_count.items()]

def sort_on(dict_item):
    return dict_item["num"]

def get_sorted_char_list(char_count):
    char_list = convert_to_list(char_count)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
