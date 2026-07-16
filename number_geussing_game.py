import random

while True:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("-" * 60)
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

    secret_number = random.randint(1, 100)

    x = int(input("Enter your choice (1-3): "))

    if x == 1:
        attempts = 10
        print("You have selected Easy mode. You have 10 chances to guess the number.")
    elif x == 2:
        attempts = 5
        print("You have selected Medium mode. You have 5 chances to guess the number.")
    elif x == 3:
        attempts = 3
        print("You have selected Hard mode. You have 3 chances to guess the number.")
    else:
        print("Invalid choice. Please select a valid difficulty level (1-3).")
        continue

    total_attempts = attempts

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess < secret_number:
            print("The number is greater than your guess.")
        elif guess > secret_number:
            print("The number is less than your guess.")
        else:
            used = total_attempts - attempts + 1
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"You guessed the number in {used} attempts.")
            break

        attempts -= 1

        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")

    if attempts == 0:
        print(f"You've run out of attempts. The number was {secret_number}. Better luck next time!")

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break
