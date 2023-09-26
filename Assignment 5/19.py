def smallest_largest_word(s):
    words = s.split()
    smallest = min(words, key=len)
    largest = max(words, key=len)
    return smallest, largest
s = "the quick brown fox jumps over the lazy dog"
smallest, largest = smallest_largest_word(s)
print(f"Smallest word: {smallest}")
print(f"Largest word: {largest}")