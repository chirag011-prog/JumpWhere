marks = float(input("Enter your marks: "))
if marks < 25:
    grade = "F"
elif 25 <= marks < 45:
    grade = "E"
elif 45 <= marks < 50:
    grade = "D"
elif 50 <= marks < 60:
    grade = "C"
elif 60 <= marks <= 80:
    grade = "B"
else:
    grade = "A"
print(f"Your grade is: {grade}")