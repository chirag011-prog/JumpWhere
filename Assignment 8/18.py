check_string = lambda s: all(cond(s) for cond in [lambda s: any(c.isupper() for c in s), 
                                                   lambda s: any(c.islower() for c in s), 
                                                   lambda s: any(c.isdigit() for c in s), 
                                                   lambda s: len(s) >= 10])

input_string = input("Enter a string: ")

if check_string(input_string):
    print("Valid string")
else:
    print("Invalid string")