items =[]

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item.")
    print("2. View items.")
    print("3. Remove an item.")
    print("4. Checkout")

    user_input = input("Choose an option: ")

    if user_input == "1":
        item = input("Item name: ")
        items.append(item)
        print(f"{item} has been added to the cart")

    elif user_input == "2":
        if not items:
            print("You have not items")
        else:
            index = 1
            for item in items:
                print(f"{index}. {item}")
    
    elif user_input == "3":
        if not items:
            print("You have no items to remove")
        else:
            for item in items:
                print(f"{index}. {item}")
                index = 1
            try:
                number_input = int(input("Which task would you like to remove: "))
                if 1 <= number_input <= len(items):
                    removed = items.pop(number_input - 1)
                    print(f"{item} has been removed. ")
            except ValueError:
                print("Invalid number")
    
    elif user_input == "4":
        break
    
    else:
        print("You can only enter numbers from 1-4")