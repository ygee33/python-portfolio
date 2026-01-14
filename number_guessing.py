import random

number = random.randint(1, 10)
attempts = 0

print("Guess a number between 1 and 10")

while True:
    guess = input("Enter your guess (or q to quit): ")

    if guess.lower() == "q":
        print("Game ended")
        break

    guess = int(guess)
    attempts += 1

    if guess == number:
        print(f"Correct! You guessed it in {attempts} tries")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
