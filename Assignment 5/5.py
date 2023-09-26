def swap_first_two_chars_and_concatenate(string1, string2):
  swapped_string1 = string2[:2] + string1[2:]
  swapped_string2 = string1[:2] + string2[2:]
  return swapped_string1 + " " + swapped_string2
swapped_string = swap_first_two_chars_and_concatenate("abc", "xyz")
print(swapped_string)