while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == "exit":
        break 

    try:
        number = int(user_input)
        if number % 2 == 0:
            print("The number is Even")
        else:
            print("The number is Odd")
    except ValueError:
        print("You can only enter numbers")