def parse_input(user_input):
    tokens = user_input.strip().split()
    cmd = tokens[0].lower() if tokens else ""
    args = tokens[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and phone number."
    name, phone = args[0], " ".join(args[1:])
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and new phone number."
    name, phone = args[0], " ".join(args[1:])
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated to {phone}."
    else:
        return f"Contact {name} not found."

def show_phone(args, contacts):
    if not args:
        return "Please provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        return f"Contact {name} not found."

def show_all_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "show":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
