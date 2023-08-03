"""
A Sample Address Book
"""

address_book = {}

def add_contact(name, phone_number):
    address_book[name] = phone_number
    print(f"Contact {name} successfully added")

def search_contact(name):
    if name in address_book:
        print(f"Contact {name} found. Number is {address_book[name]}")
    else:
        print("Contact Not Found")

def view_contacts():
    if address_book:
        print("Contacts: ")
        for name, phone_number in address_book.items():
            print(f"{name}: {phone_number}")
    else:
        print("Address Book is empty.")

def delete_contact(name):
    if name in address_book:
        del address_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")


def main():
    print("""
    Enter an option:
    
    1. View Contacts
    2. Add Contact
    3. Search Contact
    4. Delete contact
    5. Exit
    """)
    while True:
        choice = int(input("Choose btwn 1 and 5:"))

        match choice:
            case 1:
                view_contacts()
                # break
            case 2:
                name = input("Enter name: ")
                phone_number = input("Enter phone no: ")
                add_contact(name, phone_number)
                # break
            case 3:
                name = input("Name: ")
                search_contact(name)
                # break
            case 4:
                name = input("Enter the name of the contact to delete: ")
                delete_contact(name)
                # break

            case 5:
                print("Thank you for using the address book")
                exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
