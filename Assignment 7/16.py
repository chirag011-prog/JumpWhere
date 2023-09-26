def highest_3_values(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_items[:3]
    return dict(top_3)
d = {'a': 100, 'b': 300, 'c': 200, 'd': 400}
highest_values = highest_3_values(d)
print(highest_values)