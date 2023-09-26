def convert_to_uppercase(s):
    uppercase_count = sum(1 for c in s[:4] if c.isupper())
    if uppercase_count >= 2:
        return s.upper()
    else:
        return s
s = "Hello World"
print(convert_to_uppercase(s))