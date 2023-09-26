import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = ''.join(map(str, digits[:4]))
    return secret_number

def count_cows_and_bulls(secret, guess):
    cows = bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return cows, bulls

def main():
    secret = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter a 4-digit number: ")
        
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Please enter a valid 4-digit number with non-repeating digits.")
            continue
        
        attempts += 1
        cows, bulls = count_cows_and_bulls(secret, guess)

        if cows == 4:
            print(f"Congratulations!'{secret}' in {attempts} attempts.")
            break
        else:
            print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    main()
