#Python Exercise: FizzBuzz
#Write a program that prints the numbers from 1 to 50, but:
#For numbers divisible by 3, print "Fizz" instead of the number.
#For numbers divisible by 5, print "Buzz" instead of the number.
#For numbers divisible by both 3 and 5, print "FizzBuzz".
#Otherwise, print the number itself.

for number in range(50):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Bizz")
    elif number % 15 == 0:
        print("FizzBizz")
    else:
        print(number)