def get_word_count(w):
    num_words = len(w.split())
    print(f"{num_words} words found in the document")

def get_element_count(w):
    num_ele = {}
    for i in w:
        if i.lower() in num_ele:
            num_ele[i.lower()] += 1
        else:
            num_ele[i.lower()] = 1

    print(num_ele)