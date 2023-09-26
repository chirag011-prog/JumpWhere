
def replace(input_string):
    if len(input_string) < 2:
        return input_string  
    first_char = input_string[0]  
    modified_string = first_char  
    for char in input_string[1:]:
        if char == first_char:
            modified_string += '$'
        else:
            modified_string += char

    return modified_string

s=input()
print(replace(s))
