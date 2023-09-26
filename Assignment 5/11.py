def reverse_string(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s
s = "world"
print(reverse_string(s))