def are_all_dicts_empty(list_of_dicts):
    return all(not d for d in list_of_dicts)
list1 = [{}, {}, {}]
list2 = [{1, 2}, {}, {}]
print(are_all_dicts_empty(list1)) 
print(are_all_dicts_empty(list2))