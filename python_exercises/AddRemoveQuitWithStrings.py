items = []

while True:
    user_input = input("Enter command (add/remove/view/quit): ")

    if user_input.lower() == "add":
        adding_item = input("Enter item: ")
        items.append(adding_item)
        
    elif user_input.lower() == "remove":
        removing_item = input("Enter item to remove: ")
        if removing_item in items:
            items.remove(removing_item)
        else:
            print("The item you have entered is not in the list")
        
    elif user_input.lower() == "view":
        print(f"Shopping List: {items}")

    elif user_input.lower() == "quit":
        break
    
    else:
         print("Invalid command! Please enter add/remove/view/quit")


# 8===D 