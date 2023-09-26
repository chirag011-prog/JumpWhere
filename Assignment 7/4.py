my_dict = {1: 10, 2: 20, 3: 30}
def key_exists(dictionary, key):
    return key in dictionary
key_to_check = 2
if key_exists(my_dict, key_to_check):
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")