# Contact Book Manager
# This script manages a contact book, allowing the user to add new contacts and search for contacts by surname.

def add_contact(contacts: dict) -> None:
    """
    Adds a new contact to the contact dictionary.

    Args:
        contacts (dict): The contacts dictionary.
    """
    name, surname = input("\nEnter the name and surname of the new contact (separated by a space): ").split()

    if (name, surname) in contacts:
        print("\nThis person is already in the contacts.")
    else:
        phone_number = input("Enter the phone number: ")
        contacts[(name, surname)] = phone_number
        print("\nContact added.")

    print("\nCurrent contacts dictionary:", contacts)


def find_contact(contacts: dict) -> None:
    """
    Finds and displays contacts based on the given surname.

    Args:
        contacts (dict): The contacts dictionary.
    """
    search_surname = input("\nEnter the surname to search for: ").lower()

    found_contacts = [
        (name, surname, phone) for (name, surname), phone in contacts.items() if search_surname in surname.lower()
    ]

    if found_contacts:
        print("\nFound contacts:")
        for name, surname, phone in found_contacts:
            print(f"{name} {surname}: {phone}")
    else:
        print("\nContacts with this surname were not found.")


def main() -> None:
    """
    The main function to run the Contact Book Manager.
    """
    contacts = {}

    while True:
        print("\nEnter the action number:")
        print("1. Add contact")
        print("2. Find a person")
        print("3. Exit")

        choice = input("\nChoose an action: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            find_contact(contacts)
        elif choice == '3':
            print("\nExiting the Contact Book Manager.")
            break
        else:
            print("\nIncorrect choice. Please choose 1, 2 or 3.")


# Running the main function
main()
