import re
is_number = lambda s: re.match(r'^[0-9]+$', s)
string = input("Enter a string: ")
if is_number(string):
  print("The string is a number.")
else:
  print("The string is not a number.")