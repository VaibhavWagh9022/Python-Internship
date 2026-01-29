# Vaibhav Wagh
# Contact Management System

import json
from test_contacts import validate_email, validate_phone
import csv
from datetime import datetime

FILE_NAME = "contacts_data.json"
BACKUP_FILE = "contacts_backup.json"

# ---------------- FILE OPERATIONS ----------------


def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            return json.loads(content) if content else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_to_file(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def backup_contacts(contacts):
    with open(BACKUP_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- CRUD OPERATIONS ----------------
def add_contact(contacts):
    print("\n--- ADD CONTACT ---")

    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty!")
        elif name in contacts:
            print("Contact name already exists!")
        else:
            break

    while True:
        phone = input("Enter phone: ")
        phone = validate_phone(phone)
        if not phone:
            print("Invalid phone number!")
        else:
            break

    while True:
        email = input("Enter email (optional): ").strip()
        if email and not validate_email(email):
            print("Invalid email!")
        else:
            break

    address = input("Enter address (optional): ").strip()
    group = input(
        "Enter group (Friends/Work/Family/Others/Create Your own group name): ").strip() or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email or None,
        "address": address or None,
        "group": group,
        "created_at": datetime.now().isoformat()
    }

    save_to_file(contacts)
    backup_contacts(contacts)
    print("Contact added successfully!")


def search_contact(contacts):
    term = input("Enter name to search: ").lower()

    results = {
        name: info for name, info in contacts.items()
        if term in name.lower()
    }

    if not results:
        print("No contacts found.")
        return

    display_all(results)


def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    phone = input("New phone (press Enter to skip): ")
    if phone:
        phone = validate_phone(phone)
        if phone:
            contacts[name]["phone"] = phone
        else:
            print("Invalid Phone Number! Phone Number not updated")

    email = input("New email (press Enter to skip): ")
    if email and validate_email(email):
        contacts[name]["email"] = email
    else:
        print("Invalid Email! Email not Updated")

    address = input("New address (press Enter to skip): ")
    if address:
        contacts[name]["address"] = address

    group = input("New group (press Enter to skip): ")
    if group:
        contacts[name]["group"] = group

    save_to_file(contacts)
    backup_contacts(contacts)
    print("Contact updated successfully!")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == 'y':
        del contacts[name]
        save_to_file(contacts)
        backup_contacts(contacts)
        print("Contact deleted.")


def display_all(contacts):
    print("\n--- CONTACT LIST ---")
    for i, (name, info) in enumerate(contacts.items(), 1):
        print(f"{i}. {name}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info.get('email')}")
        print(f"   Address: {info.get('address')}")
        print(f"   Group: {info.get('group')}")
        print()


# ---------------- ADVANCED FEATURES ----------------
def search_by_phone(contacts):
    phone = input("Enter phone to search: ")

    for name, info in contacts.items():
        if info["phone"] == phone:
            display_all({name: info})
            return

    print("No contact found.")


def export_to_csv(contacts):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

        for name, info in contacts.items():
            writer.writerow([
                name,
                info["phone"],
                info.get("email"),
                info.get("address"),
                info.get("group")
            ])

    print("Contacts exported to CSV!")


def statistics(contacts):
    print(f"Total Contacts: {len(contacts)}")


# ---------------- USER INTERFACE ----------------
def main_menu():
    contacts = load_from_file()

    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All")
        print("6. Search by Phone")
        print("7. Export to CSV")
        print("8. Statistics")
        print("9. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_all(contacts)
        elif choice == "6":
            search_by_phone(contacts)
        elif choice == "7":
            export_to_csv(contacts)
        elif choice == "8":
            statistics(contacts)
        elif choice == "9":
            print("Thank You!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main_menu()
