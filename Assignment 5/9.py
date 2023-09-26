def remove_nth_index_char(s, n):
    if n < 0 or n >= len(s):
        return s
    return s[:n] + s[n+1:]
s = "Mangalore"
n = 4
print(remove_nth_index_char(s, n))