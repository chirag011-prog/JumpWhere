import random

def read_words_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = [line.strip() for line in file]
        return words
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

def choose_random_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman_game():
    words = read_words_file("words.txt")
    if not words:
        return

    while True:
        word_to_guess = choose_random_word(words)
        guessed_letters = []
        attempts_left = 6

        print("Welcome to Hangman!")
        print(display_word(word_to_guess, guessed_letters))

        while attempts_left > 0:
            guess = input("Guess your letter: ").upper()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in word_to_guess:
                print(display_word(word_to_guess, guessed_letters))
                if set(word_to_guess) == set(guessed_letters):
                    print("Congratulations! You guessed the word:", word_to_guess)
                    break
            else:
                attempts_left -= 1
                print("Incorrect!")
                print(f"You have {attempts_left} chances left to guess.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman_game()
