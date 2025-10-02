def get_num_words(book_content):
    return len(book_content.split())

def get_num_characters(book_content):
    book_characters = book_content.lower()
    characters_dict = {}
    for characters in book_characters:
        if characters in characters_dict:
            characters_dict[characters] += 1
        else:
            characters_dict[characters] = 1
    return characters_dict

def get_updated_dict(characters_dict):
    dict_list = []
    for char, num in characters_dict.items():
        dict_list.append({"char": char,"num": num})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    
def sort_on(item):
    return item["num"]








