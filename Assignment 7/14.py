def is_dict_empty(input_dict):
    return not bool(input_dict)
d = {}
is_empty = is_dict_empty(d)
print(f"Is the dictionary empty? {is_empty}")