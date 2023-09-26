my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
key_to_remove = "b"
if key_to_remove in my_dict:    
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed from the dictionary.")
else:
    print(f"The key '{key_to_remove}' is not in the dictionary.")
print("Updated dictionary:", my_dict)