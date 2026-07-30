from difflib import get_close_matches
from phone_utils import prepare_phone


def parse_input(user_input: str) -> tuple[str, list[str]]:
    command, *args = user_input.split()
    return command.lower(), args


def add_contact(
    name: str,
    phone: str,
    contacts: dict[str, str]
) -> str:
    if name in contacts:
        return (
            "Contact already exists. "
            "Use 'change' command to update the phone number."
        )

    phone = prepare_phone(phone)

    if phone is None:
        return "Invalid phone number."

    contacts[name] = phone
    return "Contact added."


def change_contact(
    name: str,
    phone: str,
    contacts: dict[str, str]
) -> str:
    if name not in contacts:
        return "Contact not found."

    phone = prepare_phone(phone)

    if phone is None:
        return "Invalid phone number."

    contacts[name] = phone
    return "Contact updated."


def show_phone(name: str, contacts: dict[str, str]) -> str:
    if name in contacts:
        return contacts[name]

    similar_names = get_close_matches(
        name,               # The value we want to find a similar match for
        contacts.keys(),    # The collection of available contact names
        n=1,                # Maximum number of matches to return
        cutoff=0.6          # Minimum similarity level from 0.0 to 1.0
    )

    if similar_names:
        return f"Contact not found. Did you mean '{similar_names[0]}'?"

    return "Contact not found."


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."

    return "\n".join(
        f"{name}: {phone}"
        for name, phone in contacts.items()
    )


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break

            case "hello":
                print("How can I help you?")

            case "add":
                if len(args) != 2:
                    print("Enter: add username phone")
                    continue

                name, phone = args
                print(add_contact(name, phone, contacts))

            case "change":
                if len(args) != 2:
                    print("Enter: change username phone")
                    continue

                name, phone = args
                print(change_contact(name, phone, contacts))

            case "phone":
                if len(args) != 1:
                    print("Enter: phone username")
                    continue

                print(show_phone(args[0], contacts))

            case "all":
                print(show_all(contacts))

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()