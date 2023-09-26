def match_key_values(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    for key in common_keys:
        if dict1[key] == dict2[key]:
            print(f"{key}: {dict1[key]} is present in both x and y")
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
match_key_values(x, y)