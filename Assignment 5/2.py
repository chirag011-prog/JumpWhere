s = input()
char_freq={}
for char in s:
    if char in char_freq:
        char_freq[char]+=1
    else:
        char_freq[char]=1
print(char_freq)