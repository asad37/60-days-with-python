# # Day6 File Handling & Error Handling

# # File Handling in Python
# # File handling is an important part of programming. It allows us to read from and write to files on our system.
# # In Python, we can handle files using built-in functions and methods.


# # "w" = write mode (overwrites the file if it exists)
# with open("example.txt", "w") as f:
#     f.write("Hello Asad!\n")
#     f.write("ayuwefcw cwejhvfuw uf weufwu vfwvef wef wuc wghec ghwefvghwefwefghwe fwe f weghf vwe we.\n")
# print("✅ File written successfully!")

# #inserting data into a file 
# with open("asad.text","w") as f:
#     f.write("Hello Asad Waqas")
#     f.write("ayuwefcw cwejhvfuw uf weufwu vfwvef wef wuc wghec ghwefvghwefwefghwe fwe f weghf vwe we")
# print("File written successfully!")
# #reading data of a file 
# with open("asad.text", "r") as f:
#     content=f.read()
# print(content)

# #appending to a file
# # "a" = append mode (adds new data without removing old data)
# with open("example.txt", "a") as f:
#     f.write("This line is newly added!\n")
# print("✅ Text appended to file!")

# #reading a file line by line
# with open("example.txt", "r") as f:
#     for line in f:
#         print(line.strip())
        
# # Error Handling in Python
# # Error handling is the process of responding to and recovering from error conditions in a program.
# # In Python, we can handle errors using try and except blocks.

# try:
#     with open("asad.text", "r") as f:
#         content = f.read()
#     print(content)
# except FileNotFoundError:
#     print("❌ File not found! Please check filename.")
    
##################################################
#combine above statements in one program
# filename = "notes.txt"

# while True:
#     print("\n📝 Notes App")
#     print("1. Add Note")
#     print("2. View Notes")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3): ")

#     if choice == "1":
#         note = input("Write your note: ")
#         with open(filename, "a") as f:
#             f.write(note + "\n")
#         print("✅ Note saved!")

#     elif choice == "2":
#         try:
#             with open(filename, "r") as f:
#                 notes = f.readlines()
#                 if len(notes) == 0:
#                     print("📂 No notes available.")
#                 else:
#                     print("\n📖 Your Notes:")
#                     for i, note in enumerate(notes, start=1):
#                         print(f"{i}. {note.strip()}")
#         except FileNotFoundError:
#             print("❌ No notes found. Please add a note first.")

#     elif choice == "3":
#         print("👋 Exiting Notes App. Goodbye!")
#         break

#     else:
#         print("⚠️ Invalid choice, try again.")
import os
filename="asad.txt"

while True:
    print("\n📝 Notes App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. delete Notes")
    print("4. Exit")
    
    choice =input("Enter your choice (1-3): ")
    
    if choice=="1":
        note=input("Write you note:")
        with open("asad.txt","a") as f:
            f.write(note+"\n")
        print("Note saved!")
    elif choice=="2":
        try:
            with open("asad.txt","r") as f:
                notes=f.readlines()
                if len(notes)==0:
                    print("No notes available.")
                else:
                    print("\nYour Notes:")
                    for i,note in enumerate(notes,start=1):
                        print(f"{i}. {note.strip()}")
        except FileNotFoundError:
            print("No notes found. Please add a note first.")
    elif choice == "3":
       
        if os.path.exists("asad.txt"):
            os.remove("asad.txt")
            print("All notes deleted.")
        else:
            print("No notes to delete.")
    elif choice=="4":
        print("Exiting Notes App. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")