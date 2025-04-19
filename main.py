def get_book_text(f):
    return(f.read())

def get_word_count(w):
    num_words = len(w.split())
    print(f"{num_words} words found in the document")

def main():
    with open("books/frankenstein.txt") as f:
        w = get_book_text(f)

        get_word_count(w)

main()