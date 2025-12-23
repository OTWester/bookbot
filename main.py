import sys
import stats

def main():
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Example: python3 main.py books/frankenstein.txt")
        sys.exit(1)
    
    # Get the book path from command line argument
    book_path = sys.argv[1]
    
    # Get the text
    text = stats.get_book_text(book_path)
    
    # Get word count
    word_count = stats.get_word_count(text)
    
    # Get sorted character counts
    char_count = stats.count_characters(text)
    sorted_chars = stats.get_sorted_char_list(char_count)
    
    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
