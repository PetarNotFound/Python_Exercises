contacts = []

while True: 
    name = input("Enter name: ")
    if name.lower() == "exit":
        break 

    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
    "Name": name,
    "Contact Information": phone,
    "Email": email
    }

    contacts.append(contact)

search_choice = input("Do you want to search for a contact? (yes/no): ")

if search_choice.lower() == "yes":
    search_name = input("Which name would you like to search for: ")
    found = False
    for contact in contacts:
        if contact["Name"].lower() == search_name.lower():
            print(f"\nName: {contact['Name']}, Phone: {contact['Contact Information']}, Email: {contact['Email']}")
            found = True
            break
        if not found:
            print("\nContact not found.")

            ## so pomos na chatgpt :skull: 