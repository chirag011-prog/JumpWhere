salary = int(input("Enter the salary: "))
years_of_service = int(input("Enter the year of service: "))
if years_of_service > 5:
    net_bonus = salary * 0.05
else:
    net_bonus = 0
print("Net bonus amount: ", net_bonus)
