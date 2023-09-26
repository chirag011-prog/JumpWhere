def remove_duplicates(input_dict):
    unique_dict = {}
    for key, value in input_dict.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict
d = {'a': 100, 'b': 200, 'c': 100, 'd': 300}
unique_d = remove_duplicates(d)
print(unique_d)