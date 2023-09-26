quantity = int(input("Enter the quantity: "))
unit_cost = 100
if quantity * unit_cost > 1000:
    total_cost = quantity * unit_cost * 0.9
else:
    total_cost = quantity * unit_cost
print("Total cost: ", total_cost)