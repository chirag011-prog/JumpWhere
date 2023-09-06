def anagram(str1, str2):
    if len(str1) != len(str2):
        print("not anagram")
    else:
        str1=sorted(str1)
        str2=sorted(str2)
        if str1 == str2:
            s= "anagram"
    return s        
str1=input()
str2=input()
print(anagram(str1,str2))