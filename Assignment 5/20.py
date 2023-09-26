def remove_consecutive_duplicates(s):
    result = ""
    prev_char = ""
    for char in s:
        if char != prev_char:
            result += char
            prev_char = char
    return result
s = "hello world"
print(remove_consecutive_duplicates(s))