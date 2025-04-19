from stats import get_word_count

def get_book_text(f):
    return(f.read())



def main():
    with open("books/frankenstein.txt") as f:
        w = get_book_text(f)

        get_word_count(w)

main()