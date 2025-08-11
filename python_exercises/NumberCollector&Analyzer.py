numbers = []

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")

    if user_input.lower() == "stop":
        break 
    numbers.append(int(user_input))

print("Numbers entered:")
for number in numbers:
    print(number)

print(f"Total: {sum(numbers)}" )
print(f"Count: {len(numbers)}" )
print(f"Highest: {max(numbers)}" )
print(f"Lowest: {min(numbers)}" )