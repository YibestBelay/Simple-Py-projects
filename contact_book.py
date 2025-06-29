import json
import os

CONTACT_FILE="contacts.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE,"r") as file:
            return json.load(file) 
    return {} 
 
def save_contacts(contacts):
    with open(CONTACT_FILE,"w") as file:
        json.dump(contacts,file,indent=4)

def add_contact(contacts):
    name=input("Enter a name: ").strip()
    num=input("Enter the number: ").strip()
    contacts[name]=num
    print(f"{name} ✅added Successfully.")

def view_contacts(contacts):
    if not contacts:
        print(f"❌There is no contact yet.")
    else:
        for name,phone in contacts.items():
            print(f"{name}:{phone}")    

def  search_contact(contacts):
    name=input("Enter the name: ").strip()
    if name in contacts:
        print(f" {name} - {contacts[name]}") 
        
    else:
          print(f"❌Contact is not found")

def delete_contact(contacts):
    name=input("Enter the name to delete: ").strip()
    if name  in contacts:
         del contacts[name]  
         print(f"{name} deleted")
    else:print(f"❌Contact is not found")


def main():
    contacts = load_contacts()
    while True:
        print(f"\n📗CONTACT BOOK")
        print("1. Add Contact 📝")
        print("2. View Contacts 😊")
        print("3. Search Contact 👁️")
        print("4. Delete Contact ❌")
        print("5. Exit 🔙")

        choice=input(f"choose an option: ")

        if choice=="1":
            add_contact(contacts)
        elif choice=="2":
            view_contacts(contacts)
        elif choice=="3":
            search_contact(contacts)
        elif choice=="4":
            delete_contact(contacts)
        elif choice=="5":
            save_contacts(contacts)
            print(f"Good Bye 👋")
            break
        else:
            print("❌Invalid option. Try again.")    


if __name__ == "__main__":
    main()
