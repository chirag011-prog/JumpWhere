mixed_list = [1, "apple", 3.14, 42, "banana", 2.718, "cherry", 7]
int_list = [item for item in mixed_list if isinstance(item, int)]
str_list = [item for item in mixed_list if isinstance(item, str)]
float_list = [item for item in mixed_list if isinstance(item, float)]
print("Integers:", int_list)
print("Strings:", str_list)
print("Floats:", float_list)