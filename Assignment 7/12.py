def max_min_dict_values(input_dict):
    if not input_dict:
        return None, None
    max_value = max(input_dict.values())
    min_value = min(input_dict.values())
    return max_value, min_value
d = {'a': 100, 'b': 200, 'c': 50}
max_val, min_val = max_min_dict_values(d)
print(f"Maximum value: {max_val}, Minimum value: {min_val}")