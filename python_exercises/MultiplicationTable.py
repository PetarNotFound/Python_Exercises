def multiplicationTable():
    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == "exit":
            print("Exiting Program")
            break
        
        try:
            number = int(user_input)
            for i in range(11):
                print(f"{number} * {i} = {number * i}")
        except ValueError:
            print("You can only enter numbers.")

multiplicationTable()

