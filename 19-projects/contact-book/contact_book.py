"""
Contact Book (command line)
===========================
A menu-driven address book. Contacts have a name, a phone number and an
email. They are saved to contacts.csv next to this script with the csv
module. Looking up a contact that does not exist raises a custom
exception, which the menu catches and reports.

Run: python contact_book.py

Sample session:
    Choose (1-6): 1
    Name: Asha Rai
    Phone: 9800000001
    Email: asha@example.com
    Saved Asha Rai.
    Choose (1-6): 2
    Name to search: asha
    Asha Rai             9800000001   asha@example.com
"""

import csv
from pathlib import Path

CONTACTS_FILE = Path(__file__).resolve().parent / "contacts.csv"
FIELDS = ["name", "phone", "email"]

MENU = "\n1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit"


class ContactNotFoundError(Exception):
    """Raised when no contact has the requested name."""


def load_contacts():
    """Return the saved contacts as a list of dictionaries."""
    try:
        with open(CONTACTS_FILE, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(contacts)


def find_contact(contacts, name):
    """Return the contact whose name matches (ignoring case) or raise an error."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    raise ContactNotFoundError(f"No contact named '{name}'.")


def print_contact(contact):
    print(f"{contact['name']:<20} {contact['phone']:<12} {contact['email']}")


def add_contact(contacts):
    name = input("Name: ").strip()
    if name == "":
        print("The name cannot be empty.")
        return
    try:
        find_contact(contacts, name)
        print(f"{name} is already in the book. Use Update instead.")
        return
    except ContactNotFoundError:
        pass                         # good: the name is free
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Saved {name}.")


def search_contacts(contacts):
    """Show every contact whose name contains the typed text."""
    text = input("Name to search: ").strip().lower()
    matches = [contact for contact in contacts if text in contact["name"].lower()]
    if not matches:
        print("No matching contacts.")
        return
    for contact in matches:
        print_contact(contact)


def update_contact(contacts):
    name = input("Name of the contact to update: ").strip()
    contact = find_contact(contacts, name)          # may raise ContactNotFoundError
    print("Press Enter to keep the current value.")
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email
    save_contacts(contacts)
    print(f"Updated {contact['name']}.")


def delete_contact(contacts):
    name = input("Name of the contact to delete: ").strip()
    contact = find_contact(contacts, name)          # may raise ContactNotFoundError
    contacts.remove(contact)
    save_contacts(contacts)
    print(f"Deleted {contact['name']}.")


def list_contacts(contacts):
    if not contacts:
        print("The contact book is empty.")
        return
    print(f"{'Name':<20} {'Phone':<12} Email")
    print("-" * 50)
    for contact in sorted(contacts, key=lambda c: c["name"].lower()):
        print_contact(contact)
    print(f"{len(contacts)} contact(s).")


def main():
    contacts = load_contacts()
    print(f"Contact Book ({len(contacts)} contact(s) in {CONTACTS_FILE.name})")

    actions = {
        "1": add_contact,
        "2": search_contacts,
        "3": update_contact,
        "4": delete_contact,
        "5": list_contacts,
    }
    while True:
        print(MENU)
        choice = input("Choose (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Please choose a number from 1 to 6.")
            continue
        try:
            action(contacts)
        except ContactNotFoundError as error:
            print("Error:", error)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
