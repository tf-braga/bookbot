import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()    
    return file_contents

from stats import count_characters

from stats import word_count

from stats import sort_items

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        words = get_book_text(book)
        count = count_characters(words)
        sorted = sort_items(count)
        total_words = word_count(words)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")
        for sorte in sorted:
            char = sorte["char"]
            num = sorte["num"]
            if char.isalpha():
                print(f"{char}: {num}")
        print("============= END ===============")

main()