import sys
from stats import get_word_count, get_element_count, organize_info


def get_book_text(f):
    return(f.read())


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")

        w = get_book_text(f)

        get_word_count(w)

        d = get_element_count(w)

        organize_info(d)

        print("============= END ===============")

main()