# ### 1. Number guessing game
# The program picks a random integer 1–100; the user guesses until correct.
# - **Requirements:** tell the user "higher"/"lower" after each guess; count the
#   number of attempts; reject non-numeric input without crashing.
# - **You'll learn:** `random`, `while` loops, `int()` + exceptions, conditionals.
# - **Stretch:** add difficulty levels (limited attempts); play-again loop.

import random

target_number = random.randint(0, 100)
guess_taken = 0

print("Welcome to number guessing game!")
print("You win when you guess the correct number! (0-100) inclusive")
print("Let's begin.")

while True:
    guess_taken += 1
    raw = input("Your guess: ")

    try:
        guess_number = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        guess_taken -= 1
        continue

    if guess_number == target_number:
        print("Your guess is correct. Congratulation!")
        print(f"Guess taken: {guess_taken}")
        play_again = str(input("Want to play again? (y/n)"))

        if play_again == "y":
            guess_taken = 0
            target_number = random.randint(0, 100)
            continue

        break

    if guess_number > 100:
        print("The number is lesser or equal to 100")
        continue

    if guess_number < 0:
        print("The number is greater or equal to 0")
        continue

    if guess_number < target_number:
        print("Greater")
        continue

    if guess_number > target_number:
        print("Lesser")
        continue
