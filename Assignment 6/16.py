user_list = input("Enter elements separated by spaces: ").split()
element_to_delete = input("Enter an element to delete from the list: ")
user_list = [int(x) for x in user_list]
if element_to_delete in user_list:
    user_list.remove(int(element_to_delete))
    print(f"{element_to_delete} was found and deleted from the list.")
else:
    print(f"{element_to_delete} was not found in the list.")
print("List after deletion:")
for element in user_list:
    print(element)