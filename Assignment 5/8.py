def longest_word_length(words):
    return max(len(word) for word in words)
words = ["I", "love", "my", "country"]
print(longest_word_length(words))