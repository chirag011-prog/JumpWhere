def extend_list_without_append(list1, list2):
    list1[:0] = list2
list1 = [10, 20, 30]
list2 = [40, 50, 60]
extend_list_without_append(list1, list2)
print(list1)