incomplete_tasks = []
complete_tasks = [] 

while True:
    user_input = input("Use (add, view, quit) to add and view tasks or quit to exit the program: ")

    if user_input.lower() == "add":
        description = input("Enter task description: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        complete = input("Is the task complete/incomplete: ")

        if complete.lower() == "complete":
            task = {
                "task": description,
                "deadline": deadline,
                "done": True
                }
            complete_tasks.append(task)
        elif complete.lower() == "incomplete":
            task = {
                "task": description,
                "deadline": deadline,
                "done": False
                }
            incomplete_tasks.append(task)
    
    elif user_input.lower() == "view":
        print("\nIncomplete Tasks:")
        for idx, task in enumerate(incomplete_tasks, start=1):
            print(f"{idx}. {task["task"]} (Due: {task["deadline"]})")

        print("\nComplete Tasks:")
        for idx, task in enumerate(complete_tasks, start=1):
            print(f"{idx}. {task["task"]} (Due: {task["deadline"]})")

    elif user_input.lower() == "quit":
        print("Exiting")
        break 