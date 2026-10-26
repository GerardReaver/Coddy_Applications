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
    name = input()
    if name in contact_book:
        print("Contact already exists!")
    else:
        phone = input()
        email = input()
        address = input()
        contact_book[name] = {
            "phone": phone,
            "email": email, 
            "address": address
            }
        print("Contact added successfully!")
