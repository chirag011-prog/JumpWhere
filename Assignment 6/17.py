def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
all_numbers = list(range(1, 101))
even_numbers = [num for num in all_numbers if num % 2 == 0]
odd_numbers = [num for num in all_numbers if num % 2 != 0]
prime_numbers = [num for num in all_numbers if is_prime(num)]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Prime numbers:", prime_numbers)