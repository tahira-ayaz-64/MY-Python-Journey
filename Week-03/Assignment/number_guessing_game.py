                 

import random

 # secret_number = random.randint(1, 20)

secret_number = 12
attempts = 0
max_attempts = 5
won = False

while attempts < max_attempts:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        won = True
        break

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Too low!")

    
if not won:
    print("Game over! You used all your attempts.")
    print("The secret number was:", secret_number)