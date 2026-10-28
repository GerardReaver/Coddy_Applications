# Create a function called display menu
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
    
# Create a function to add a contact
def add_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        phone = input("Enter contact number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        contact_book[name] = {
            "phone": phone,
            "email": email, 
            "address": address
            }
        print("Contact added successfully!")

# Create a function called view contact
def view_contact(contact_dict):
    contact_name = input("Enter contact name: ")
    if contact_name not in contact_dict:
        print("Contact not found!")
    else:
        name = contact_name
        phone = contact_dict[contact_name]["phone"]
        email = contact_dict[contact_name]["email"]
        address = contact_dict[contact_name]["address"]
        print("Name:", name)
        print("Phone:", phone)
        print("Email:", email)
        print("Address:", address)

# Create a function to edit contacts
def edit_contact(contact_book):
    edit_name = input("Enter the name you would like to edit: ")
    if edit_name in contact_book:
        new_phone = input("Enter the new number: ")
        if new_phone == "":
            new_phone = contact_book[edit_name]["phone"]
        new_email = input("Enter the new email: ")
        if new_email == "":
            new_email = contact_book[edit_name]["email"]
        new_address = input("Enter the new address: ")
        if new_address == "":
            new_address = contact_book[edit_name]["address"]
        contact_book[edit_name] = {
            "phone": new_phone,
            "email": new_email,
            "address": new_address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Create a function to delete a contact
def delete_contact(contact_book):
    delete_name = input("Type name to delete: ")
    if delete_name in contact_book:
        contact_book.pop(delete_name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Create a function to list all the contacts
def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for keys, values in contact_book.items():
            print(f"Name: {keys}")
            print(f"Phone: {values['phone']}")
            print(f"Email: {values['email']}")
            print(f"Address: {values['address']}")
            print("")

# Creating the final function to put it all together
def contact_book_app():
    contact_book = {}
    while True:
        display_menu()
        user_input = input("Type in a number choice: ")
        if user_input == "1":
            add_contact(contact_book)
        elif user_input == "2":
            view_contact(contact_book)
        elif user_input == "3":
            edit_contact(contact_book)
        elif user_input == "4":
            delete_contact(contact_book)
        elif user_input == "5":
            list_all_contacts(contact_book)
        elif user_input == "6":
            break 
        else:
            print("Invalid choice. Please try again.")
# Actually call the function. Happy Coding!
contact_book_app()
