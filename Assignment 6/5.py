def main():
    n = 0
    sum = 0
    while True:
        num = int(input("Enter an integer number (0 to finish): "))
        if num == 0:
            break
        n += 1
        sum += num
    if n == 0:
        print("No numbers entered.")
    else:
        average = sum / n
        print(f"Sum of the numbers: {sum}")
        print(f"Average of the numbers: {average}")
if __name__ == "__main__":
    main()