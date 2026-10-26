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
# Create a function called view contact
def view_contact(contact_dict):
    contact_name = input()
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
