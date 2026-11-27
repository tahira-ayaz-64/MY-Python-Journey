
import random

# Generate a random secret number
secret_number = random.randint(1, 20)

# Set maximum attempts
attempts = 0
max_attempts = 5
won = False

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 20.")
print("You have 5 attempts.")

# Continue until attempts are finished
while attempts < max_attempts:

    try:
        guess = int(input("Enter your guess: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Check whether the number is within range
    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.")
        continue

    # Increase attempts after a valid guess
    attempts += 1

    # Compare guess with secret number
    if guess == secret_number:
        won = True
        print("Congratulations! You guessed correctly.")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Too low!")

    # Display attempts used and remaining
    print("Attempts used:", attempts)
    print("Attempts remaining:", max_attempts - attempts)

    if won:
        break

# Display losing message
if not won:
    print("Game over! You used all your attempts.")
    print("The secret number was:", secret_number)

print("Thanks for playing!")
