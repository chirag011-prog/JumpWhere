def unique_sorted_words(words):
    unique_words = set(words.split(','))
    return sorted(unique_words)
words = "red, white, black, red, green, black"
print(unique_sorted_words(words))