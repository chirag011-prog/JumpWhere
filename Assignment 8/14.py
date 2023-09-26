def starts_with(string, character):
  return string[0] == character
string = input("Enter a string: ")
character = input("Enter a character: ")
if starts_with(string, character):
  print("The string starts with the character.")
else:
  print("The string does not start with the character.")