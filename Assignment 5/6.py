def add_ing_or_ly(string):
    if len(string) < 3:
        return string
    if string.endswith("ing"):
        return string + "ly"
    return string + "ing"
string_with_added_suffix = add_ing_or_ly("abc")
print(string_with_added_suffix)
string_with_added_suffix = add_ing_or_ly("string")
print(string_with_added_suffix)