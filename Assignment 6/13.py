total = 0
count = 0
for i in range(10):
    num = int(input("Enter an integer: "))
    total += num
    count += 1
average = total / count
print(f"The average of the 10 integers is: {average}")
