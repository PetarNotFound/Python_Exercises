while True:

    first_input = input("Enter your first number: ")
    second_input = input("Enter your second number: ")
    op = input("Which operator woul you like to perform (+, -, *, /): ")

    try:
        first = int(first_input)
        second = int(second_input)
        if op == "+":
            print(f"{first} + {second} = {first + second} ")
        elif op == "-":
            print(f"{first} - {second} = {first - second} ")
        elif op == "*":
            print(f"{first} * {second} = {first * second} ")
        elif op == "/":
            if second == 0:
                print("Can not divide by zero")
            else:
                print(f"{first} + {second} = {first / second} ")
    except ValueError:
        print("You can only enter numbers or 'cancel' to quit the program")