import re

contacts = {}

def main_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Quit")

def valid_phone(phone):
    pattern = r'^\+?[\d\s\(\)-]{7,15}$'
    return re.match(pattern, phone) is not None

def valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    
    if not  valid_phone(phone):
        print("Invalid phone number format.")
        return
    
    email = input("Enter email address: ").strip()
    
    if not valid_email(email):
        print("Invalid email address format.")
        return

    address = input("Enter address: ").strip()
    notes = input("Enter any notes: ").strip()

    contact_id = phone if phone else email
    contacts[contact_id] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'notes': notes }

    print("Contact added successfully!")

def edit_contact():
    print("\n--- Edit Existing Contact ---")
    contact_id = input("Enter the phone number or email of the contact to edit: ").strip()

    if contact_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[contact_id]
    print(f"Editing contact for {contact['name']}")

    name = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ").strip() or contact['name']
    phone = input(f"Enter new phone (or press Enter to keep '{contact['phone']}'): ").strip() or contact['phone']
    
    if phone != contact['phone'] and not valid_phone(phone):
        print("Invalid phone number format.")
        return

    email = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ").strip() or contact['email']
    
    if email != contact['email'] and not valid_email(email):
        print("Invalid email address format.")
        return

    address = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ").strip() or contact['address']
    notes = input(f"Enter new notes (or press Enter to keep '{contact['notes']}'): ").strip() or contact['notes']

    contacts[contact_id] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'notes': notes
    }

    print("Contact updated successfully!")

def delete_contact():
    print("\n--- Delete Contact ---")
    contact_id = input("Enter the phone number or email of the contact to delete: ").strip()

    if contact_id not in contacts:
        print("Contact not found.")
        return

    del contacts[contact_id]
    print("Contact deleted successfully!")

def search_contact():
    print("\n--- Search for Contact ---")
    contact_id = input("Enter the phone number or email of the contact to search for: ").strip()

    if contact_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[contact_id]
    print(f"Contact found: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")
    print(f"Notes: {contact['notes']}")

def display_all_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return

    for contact_id, contact in contacts.items():
        print(f"\n{contact['name']} ({contact_id})")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print(f"Notes: {contact['notes']}")

def export_contacts():
    print("\n--- Export Contacts ---")
    filename = input("Enter the filename to save contacts (e.g., contacts.txt): ").strip()

    try:
        with open(filename, 'w') as file:
            for contact_id, contact in contacts.items():
                file.write(f"{contact['name']} ({contact_id})\n")
                file.write(f"Phone: {contact['phone']}\n")
                file.write(f"Email: {contact['email']}\n")
                file.write(f"Address: {contact['address']}\n")
                file.write(f"Notes: {contact['notes']}\n")
                file.write("-" * 40 + "\n")
        print(f"Contacts exported to {filename} successfully!")
    except Exception as e:
        print(f"Error exporting contacts: {e}")
def main():
    while True:
        main_menu()
        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == '1':
                add_contact()
            elif choice == '2':
                edit_contact()
            elif choice == '3':
                delete_contact()
            elif choice == '4':
                search_contact()
            elif choice == '5':
                display_all_contacts()
            elif choice == '6':
                export_contacts()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()