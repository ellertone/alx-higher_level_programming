#!/usr/bin/python3
"""
A simple guessing game
"""

import random


def main():
    secretNumber = random.randint(0, 100)
    MAX_TRIES = 7
    attempts = 0


    while attempts < MAX_TRIES:
        print(f"""
        Enter a number between 1 and 100.
        You have {MAX_TRIES}
        You have made {attempts} tries
            """)

        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue



            attempts += 1

            if guess == secretNumber:
                print("You have found the answer")
                break
            elif guess < secretNumber:
                print("Too low! Try again.")
            else:
                print("Too high! Try again")
        except ValueError:
            print("Please enter a valid number")

    else:
        print(f"Sorry, you've run out of attempts. The secret number was {secretNumber}.")

if __name__ == "__main__":
    main()
