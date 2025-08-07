#Python Exercise: Simple Number Guessing Game
#Write a Python program where the user has to guess a number between 1 and 10.

import random 

rand = random.randint(1, 10)

while True:
    user_input = (input("Guess the number from 1 to 10: "))

    try:
        guess = int(user_input)
        if guess == rand:
            print("Correct!")
            break
        elif guess != rand:
            print("Incorrect")
    except ValueError:
        print("You can only enter numbers.")

print(f"The number was : {rand}")