def replace_not_poor_with_good(string):
  not_poor_index = string.find("not poor")
  if not_poor_index != -1:
    return string[:not_poor_index] + "good" + string[not_poor_index + 8:]
  return string
string_with_replaced_substring = replace_not_poor_with_good("The lyrics is not that poor!")
print(string_with_replaced_substring)
string_with_replaced_substring = replace_not_poor_with_good("The lyrics is poor!")
print(string_with_replaced_substring)
