def remove_duplicates_from_list_of_lists(lst):
    seen = set()
    result = []
    for sublist in lst:
        if tuple(sublist) not in seen:
            result.append(sublist)
            seen.add(tuple(sublist))
    return result
my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = remove_duplicates_from_list_of_lists(my_list)
print(new_list)