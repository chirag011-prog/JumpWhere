def sort_dict_by_key(input_dict):
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict
d = {'b': 200, 'a': 100, 'c': 300}
sorted_d = sort_dict_by_key(d)
print(sorted_d)