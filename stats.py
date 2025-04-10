def get_num_words(file_contents):    
    num_words = len(file_contents.split())
    return num_words

def get_char_count(file_contents):
    char_dict = {}
    for char in file_contents.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def report_char_count(char_dict):
    char_count_list = []
    for char, count in char_dict.items():
        char_count_list.append({"char": char, "num": count})
    
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list
