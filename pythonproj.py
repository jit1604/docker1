import random  # To generate a random number

secret_number = random.randint(1, 100)

print(" Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("Too low!  Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(" Correct! You guessed it!")
        break