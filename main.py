import sys
from stats import get_num_words, get_num_characters, get_updated_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = get_num_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_characters = get_num_characters(book_content)
    sorted_chars = get_updated_dict(num_characters)
   
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()