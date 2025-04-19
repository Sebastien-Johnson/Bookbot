from stats import get_word_count, get_element_count, organize_info

def get_book_text(f):
    return(f.read())


def main():
    with open("books/frankenstein.txt") as f:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {f.name}...")
        w = get_book_text(f)

        get_word_count(w)

        d = get_element_count(w)

        organize_info(d)
        print("============= END ===============")

main()