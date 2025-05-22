def get_num_words(text):
    words = text.split()
    result = len(words)
    print(f"Found {result} total words")
  
def get_characters(text):
    words = text.split()
    chars = [char.lower() for string in words for char in string]
    result = {}

    for char in chars:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(dict):
    return dict["num"]

def get_report(text):
    char_dict = get_characters(text)
    dict_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            dict_list.append({"char":char, "num":count})
    
    dict_list.sort(reverse=True, key=sort_on)

    for char in dict_list:
        print(f"{char['char']}: {char['num']}")
  