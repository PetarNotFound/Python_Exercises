print("Menu: start, stop, help, quit")

while True:
    user_input = input("Enter a command: ")

    match user_input:
        case "start":
            print("Starting the program...")
        case "stop":
            print("Stopping the program.")
        case "help":
            print("Vailable commands: start, stop, help, quit")
        case "quit":
            print("Goodbye!")
            break 