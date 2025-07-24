def get_num_words(text_string):
    splitted_text = text_string.split()
    num_words = len(splitted_text)
    print(f"{'-'*10} Word Count {'-'*10}")
    print(f"Found {num_words} total words")



def get_chars_dict(text_string):
    chars = {}
    for c in text_string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

def sort_chars_dict(chars_dict):
    list_dict = [{"char": k, "num": v} for k, v in chars_dict.items()]
    list_dict.sort(reverse=True, key=lambda x: x["num"])
    return list_dict
