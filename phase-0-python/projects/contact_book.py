from pydantic import BaseModel
import json
from datetime import datetime

menu_option = "(1) Add contact\n(2) Search by name\n(3) List all\n(4) Delete\n(5) Quit"

class Contact(BaseModel):
    name: str
    phone: str
    email: str
    last_modified: datetime

contact_list: list[Contact] = []

def is_valid_email(email: str):
    return "@" in email

def is_contact_exist(name: str):
    for contact in contact_list:
        if contact.name.lower() == name.lower():
            return True
    return False

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    if is_valid_email(email):
        if is_contact_exist(name):
            accept = input((f"{name} already exist! Overwrite? Y/N"))
            if accept.lower() == "y":
                for index, contact in enumerate(contact_list):
                    if contact.name.lower() == name.lower():
                        contact_list[index].name = name
                        contact_list[index].phone = phone
                        contact_list[index].email = email
                        contact_list[index].last_modified = datetime.now()
                        print(f"{name} updated!")
            else:
                print("Contact not added!")
        else:
            contact_list.append(Contact(name =name, phone = phone, email= email, last_modified =datetime.now()))
            print(f"{name} added!")
    else:
        print("Invalid email")

def search_by_name(name: str):
    for contact in contact_list:
        if contact.name.lower() == name.lower():
            return contact

def list_all():
    if not contact_list:
        print("No contacts yet!")
    for contact in contact_list:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def delete_contact(name: str):
    for contact in contact_list:
       if contact.name.lower() == name.lower():
            contact_list.remove(contact)
            return True
    
    return False

def load_contacts():
    try:
        with open("phase-0-python/week-2/output-files/contact.json", "r") as f:
            contact_json_list = json.load(f)
            for contact_json in contact_json_list:
                contact_list.append(Contact(**contact_json))
        return contact_list
    except FileNotFoundError:
        print("file not found!")
        return []

def save_contacts():
    with open("phase-0-python/week-2/output-files/contact.json", "w") as f:
        json_contacts_list = []
        for contact in contact_list:
            json_contacts_list.append(contact.model_dump(mode="json"))
        json.dump(json_contacts_list, f, indent = 2)

load_contacts()

while True:
    print(menu_option)
    choice = int(input("Choose: "))
    if choice == 5:
        save_contacts()
        break
    elif choice == 1:
        add_contact()
    elif choice == 2:
        name = input("Name: ")
        res = search_by_name(name)
        if res:
            print(res)
        else:
            print("Contact not found")
    elif choice == 3:
        list_all()
    elif choice == 4:
        name = input("Enter contact name to delete: ")
        success = delete_contact(name)
        if success:
            print(f"{name} deleted")
        else:
            print("contact not found")
    else:
        print("Invalid choice, please try again")