import random

def main():
    low = 1
    high = 1000
    secretNumber = random.randint(0, 1000)
    attempts = 0
    MAX_TRIES = 10

    while attempts < MAX_TRIES:
        guess = (low + high)//2

        print(f"Attempt {attempts + 1}: Guessing {guess}")

        # Check if the guess is correct
        if guess == secretNumber:
            print(f"Congratulations! You guessed the secret number {secretNumber} in {attempts + 1} attempts!")
            break
        elif guess < secretNumber:
            print("Too low! Guess higher.")
            low = guess + 1  # Adjust the lower bound for the next guess
        else:
            print("Too high! Guess lower.")
            high = guess - 1  # Adjust the upper bound for the next guess

        attempts += 1

    else:
        print(f"Sorry, you've run out of attempts. The secret number was {secretNumber}.")

if __name__ == "__main__":
    main()
