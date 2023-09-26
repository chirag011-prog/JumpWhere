def count_repeated_chars(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count
s = "thequickbrownfoxjumps over the lazy dog"
char_count = count_repeated_chars(s)
for char, count in char_count.items():
    print(f"{char}: {count}")