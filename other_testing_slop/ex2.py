print("Printing current and previous number sum in range(10)")

for current_number in range(11):
    previous_number = current_number - 1
    sum = previous_number + current_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {sum}")