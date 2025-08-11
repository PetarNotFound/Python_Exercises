secret_words = ["apple", "banana", "cherry"]
while True:
    user_input = input("Guess the secret word: ")

    if user_input in secret_words:
        print("You guessed it!")
        break
    else:
        print("Try again!")

print("The secret words were: ")
for word in secret_words:
    print(word)