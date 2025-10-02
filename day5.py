# # Dictionaries Key Values Pairs


# # A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.


# student={
#     'name':'Asad',
#     'age':23,
#     'country':'Pakistan',
#     'profession':'Software Engineer',
#     "fav_programing_language": "Python"
# }
# # student['age']=24 #updating value
# # student["city"]="Lahore" #adding new key value pair
# # del student['profession'] #deleting key value pair

# # print(student)
# # print(student['name'])
# # print(student['age'])
# student['age']=24
# student["city"]="Lahore"

# for key, value in student.items():
#     print(f"{key}:{value}")
    
    
    
# # Tuples
# # A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# #Tuple is immmutable (unchangeable)
# fruits=("Apple","Banana","Mango","Orange")
# print(fruits)
# print(fruits[0])
# for num in fruits:
#     print(num)
    
# # fruits[0]="Grapes" #This will give error because tuple is immutable

# students={
#     "101":("Asad",23,"Pakistan"),
#     "102":("Ali",22,"India"),
#     "103":("Ahmed",24,"USA"),
#     "104":("Ahsan",21,"UK"),
#     "105":("Adeel",25,"Canada"),
#     "106":("Amir",23,"Australia")
# }

# for roll_no, detail in students.items():
#     print(f"Roll No:{roll_no}")
#     print(f"Name:{detail[0]}")
#     print(f"Age:{detail[1]}")
#     print(f"Country:{detail[2]}")
#     print("#########################")
    
    
    
    ########################################
    
    
# phonebook={}
    
# while True:
#     print("\n--- Phonebook Menu ---")
#     print("1. Add contact")
#     print("2. Remove contact")
#     print("3. View contacts")
#     print("4. Exit")
        
#     choice = input("Enter your choice (1-4): ")
        
#     if choice =="1":
#             name=input("Enter contact name: ")
#             phone=input("Enter contact phone number: ")
#             phonebook[name]=phone
#             print(f"{name} added to phonebook.")
#     elif choice =="2":
#             name=input("Enter contact name to remove: ")
#             if name in phonebook:
#                 del phonebook[name]
#                 print(f"{name} removed from phonebook.")
#             else:
#                 print("Contact not found in phonebook.")
#     elif choice =="3":
#             print("\nYour Contacts:")
#             if len(phonebook)==0:
#                 print("Phonebook is empty.")
#             else:
#                 for name, phone in phonebook.items():
#                     print(f"{name}: {phone}")
#     elif choice =="4":
#             print("Exiting phonebook. Goodbye!")
#             break
#     else:
#             print("Invalid choice! Please try again.")
##########################################
phonebook={}
while True:
    print("\n--- Phonebook Menu ---")
    
    print("1. Add contact")
    print("2. Remove contact")
    print("3. View contacts")
    print("4. Exit")
    
    choice =input("Enter your choice (1-4): ")
    
    if choice =="1":
        name=input("Enter contact name: ")
        phone=input("Enter contact phone number: ")
        phonebook[name]=phone
        print(f"{name} added to phonebook.")
    elif choice =="2":
        name=input("Enter Contact name to remove: ")
        if name in phonebook:
            del phonebook[name]
            print(f"{name} removed from phonebook.")
        else:
            print("Contact not found in phonebook.")
    elif choice =="3":
        print("\nYour Contacts:")
        if len(phonebook)==0:
            print("Phonebook is empty.")
        else:
            for name, phone in phonebook.items():
                print(f"{name}:{phone}")
    elif choice =="4":
        print("Exiting phonebook. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
        
        
        
##########################################
phonebook = {}

while True:
    print("\n📱 Phonebook Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Search Contact (by name)")
    print("6. Save Phonebook to File")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        phonebook[name] = number
        print(f"✅ {name} added successfully!")

    elif choice == "2":
        name = input("Enter contact name to view: ")
        if name in phonebook:
            print(f"{name} → {phonebook[name]}")
        else:
            print("❌ Contact not found!")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"🗑️ {name} deleted successfully!")
        else:
            print("❌ Contact not found!")

    elif choice == "4":
        if len(phonebook) == 0:
            print("📂 Phonebook is empty.")
        else:
            print("\n📖 All Contacts:")
            for name, number in phonebook.items():
                print(f"{name} → {number}")

    elif choice == "5":  # 🔍 Search by partial name
        search = input("Enter name to search: ").lower()
        results = {name: number for name, number in phonebook.items() if search in name.lower()}
        
        if results:
            print("\n🔍 Search Results:")
            for name, number in results.items():
                print(f"{name} → {number}")
        else:
            print("❌ No matching contacts found.")

    elif choice == "6":  # 💾 Save phonebook to file
        with open("phonebook.txt", "w") as f:
            for name, number in phonebook.items():
                f.write(f"{name}: {number}\n")
        print("💾 Phonebook saved to 'phonebook.txt' successfully!")

    elif choice == "7":
        print("👋 Exiting Phonebook. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice, try again.")
##########################################
import os

phonebook = {}

# 📂 Load contacts from file at startup
if os.path.exists("phonebook.txt"):
    with open("phonebook.txt", "r") as f:
        for line in f:
            if ":" in line:
                name, number = line.strip().split(": ")
                phonebook[name] = number

while True:
    print("\n📱 Phonebook Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Search Contact (by name)")
    print("6. Save Phonebook to File")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        phonebook[name] = number
        print(f"✅ {name} added successfully!")

    elif choice == "2":
        name = input("Enter contact name to view: ")
        if name in phonebook:
            print(f"{name} → {phonebook[name]}")
        else:
            print("❌ Contact not found!")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"🗑️ {name} deleted successfully!")
        else:
            print("❌ Contact not found!")

    elif choice == "4":
        if len(phonebook) == 0:
            print("📂 Phonebook is empty.")
        else:
            print("\n📖 All Contacts:")
            for name, number in phonebook.items():
                print(f"{name} → {number}")

    elif choice == "5":  # 🔍 Search by partial name
        search = input("Enter name to search: ").lower()
        results = {name: number for name, number in phonebook.items() if search in name.lower()}
        
        if results:
            print("\n🔍 Search Results:")
            for name, number in results.items():
                print(f"{name} → {number}")
        else:
            print("❌ No matching contacts found.")

    elif choice == "6":  # 💾 Save phonebook to file
        with open("phonebook.txt", "w") as f:
            for name, number in phonebook.items():
                f.write(f"{name}: {number}\n")
        print("💾 Phonebook saved to 'phonebook.txt' successfully!")

    elif choice == "7":  # 👋 Exit and auto-save
        with open("phonebook.txt", "w") as f:
            for name, number in phonebook.items():
                f.write(f"{name}: {number}\n")
        print("👋 Exiting Phonebook. Contacts saved automatically. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice, try again.")
