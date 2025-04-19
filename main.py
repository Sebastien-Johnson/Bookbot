def get_book_text(f):
    print(f.read())

def main():
    with open("books/frankenstein.txt") as f:
        get_book_text(f)

main()