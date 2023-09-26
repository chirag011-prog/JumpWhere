total = 0
count = 0
product = 1
while True:
    user_input = input("Enter an integer (press 'q' to quit): ")
    if user_input.lower() == 'q':
            break
    num = int(user_input)
    total += num
    product *= num
    count += 1
if count > 0:
    average = total / count
    print(f"Average  {average}")
    print(f"Product{product}")
else:
    print("No numbers were entered.")