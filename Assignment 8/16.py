original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisible_by_nineteen_or_thirteen = list(filter(lambda x: (x % 19 == 0) or (x % 13 == 0), original_list))
print(divisible_by_nineteen_or_thirteen)