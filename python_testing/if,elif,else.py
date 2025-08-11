grade = int(input("Enter your score: "))

if 90 <= grade <= 100:
    print("Your grade is A")
elif 80 <= grade <= 89:
    print("Your grade is B")
elif 70 <= grade <= 79:
    print("Your grade is C")
elif 60 <= grade <= 69:
    print("Your grade is D")
elif 0 <= grade < 60:
    print("Your grade is F")
else:
    print("You can only enter numbers from 0-100")