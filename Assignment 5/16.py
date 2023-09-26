def print_index(s, c):
    for i, char in enumerate(s):
        if char == c:
            print(i)
s = "hello world"
c = "o"
print_index(s, c)