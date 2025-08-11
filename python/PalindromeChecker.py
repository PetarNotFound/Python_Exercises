user_input = input("Enter a word: ")

word_no_spaces = user_input.replace(" ", "")
word = word_no_spaces.lower()
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")