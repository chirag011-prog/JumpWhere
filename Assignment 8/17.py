original_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
sorted_matrix = sorted(original_matrix, key=lambda x: sum(x))
print(sorted_matrix)
original_matrix = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sorted_matrix = sorted(original_matrix, key=lambda x: sum(x))
print(sorted_matrix)