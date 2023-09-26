d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = {}
for key, value in d1.items():
    combined_dict[key] = combined_dict.get(key, 0) + value
for key, value in d2.items():
    combined_dict[key] = combined_dict.get(key, 0) + value
print(combined_dict)