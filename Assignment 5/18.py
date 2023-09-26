def swap_comma_dot(s):
    return s.replace(",", "__temp__").replace(".", ",").replace("__temp__", ".")
s = "32.054,23"
print(swap_comma_dot(s))