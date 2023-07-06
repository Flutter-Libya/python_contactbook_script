class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone):
        for contact in self.contacts:
            if contact.name == name:
                print(f'Contact {name} already exists.')
                return
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def delete(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def view(self):
        for contact in sorted(self.contacts, key=lambda contact: contact.name):
            print(f'Name: {contact.name}, Phone: {contact.phone}')

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact\n2. Delete Contact\n3. View Contacts\n4. Quit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter the name of the contact: ")
            phone = input("Enter the phone number of the contact: ")
            if not phone.isdigit():
                print("Invalid phone number. Please enter only digits.")
                continue
            contact_book.add(name, phone)
        elif choice == 2:
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete(name)
        elif choice == 3:
            contact_book.view()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
