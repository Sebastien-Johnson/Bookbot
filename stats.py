def get_word_count(w):
    num_words = len(w.split())
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_element_count(w):
    num_ele = {}
    for i in w:
        if i.lower() in num_ele:
            num_ele[i.lower()] += 1
        else:
            num_ele[i.lower()] = 1

    return num_ele


def organize_info(d):
    orged_info = []

    for i in d:
        if i.isalpha() == True:
            orged_info.append({"element" : i, "num" : d[i]})    

    def sort_on(orged_info):
        return orged_info["num"]

    orged_info.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    
    for i in orged_info:
        print(f"{i["element"]}: {i["num"]}")