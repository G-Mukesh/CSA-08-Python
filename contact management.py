import csv

contacts_file = 'contacts.csv'

#Load and display the contacts
def load_contacts(): 
    contacts = []
    try:
        with open(contacts_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        pass  # No contacts file found, starting with an empty list
    return contacts

# Function to save contacts to file
def save_contacts(contacts):
    with open(contacts_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    print()

# Adds a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print("Contact added successfully.")

#Deletes the existing contact
def delete_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Updates the contacts
def update_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input("Enter the contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")

            if name:
                contacts[index][0] = name
            if phone:
                contacts[index][1] = phone
            if email:
                contacts[index][2] = email

            save_contacts(contacts)
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to search for contacts
def search_contacts(contacts):
    query = input("Enter name, phone, or email to search: ").lower()
    results = [contact for contact in contacts if query in contact[0].lower() or query in contact[1] or query in contact[2].lower()]
    
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
        print()
    else:
        print("No contacts found.")

# Main function to run the contact management system
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Display all contacts")
        print("2. Add a new contact")
        print("3. Delete a contact")
        print("4. Update a contact")
        print("5. Search contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            search_contacts(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
