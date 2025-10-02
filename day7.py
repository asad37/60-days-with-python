#Day7 CSV Handling in Python
#CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. Each line in a CSV file corresponds to a row in the table, and each value in the row is separated by a comma.
#CSV files can be easily created and edited using a text editor or spreadsheet software like Microsoft Excel or Google Sheets. They are widely used for data exchange between different applications and platforms due to their simplicity and compatibility.
# import csv 

# students=[
#     ["Asad",23,"Pakistan","Software Engineer"],
#     ["Ali",22,"India","Data Scientist"],
#     ["Ahmed",24,"USA","Web Developer"],
#     ["Ahsan",21,"UK","System Analyst"],
#     ["Adeel",25,"Canada","Network Engineer"],
#     ["Amir",23,"Australia","Database Administrator"]
# ]

# #writing to a csv file
# with open("students.csv","w",newline='') as f:
#     writer=csv.writer(f)
#     writer.writerows(students)
# print("CSV file written successfully!")


# with open("students.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# import csv 
# import os
# filename="expanses.csv"


# if not os.path.exists(filename):
#     with open(filename, "w", newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(["Date", "Description", "Amount"])
#     print("CSV file created successfully!")
    
    
    
# while True:
#     print("\n--- Expense Tracker Menu ---")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3): ")

#     if choice == "1":
#         date = input("Enter date (YYYY-MM-DD): ")
#         description = input("Enter description: ")
#         amount = input("Enter amount: ")

#         with open(filename, "a", newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow([date, description, amount])
#         print("✅ Expense added!")

#     elif choice == "2":
#         try:
#             with open(filename, "r") as f:
#                 reader = csv.reader(f)
#                 next(reader)  # Skip header row
#                 print("\nYour Expenses:")
#                 for row in reader:
#                     print(f"- Date: {row[0]}, Description: {row[1]}, Amount: Rs.{row[2]}")
#         except FileNotFoundError:
#             print("No expenses found. Please add an expense first.")

#     elif choice == "3":
#         print("Exiting Expense Tracker. Goodbye!")
#         break

#     else:
#         print("⚠️ Invalid choice, try again.")
        
# import csv 
# import os 

# filename="expanses.csv"      
        
# if not os.path.exists(filename):
#     with open(filename,"w",newline='')as f:
#        writer=csv.writer(f)
#        writer.writerow(["Date", "Description", "Amount"])
#     print("CSV file created successfully!")   
    
# while True:
#     print("\n--- Expense Tracker Menu ---")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Exit")
#     choice =input("Enter your choice (1-3): ")
#     if choice=="1":
#         date=input("Enter date (yyyy-mm-dd):")
#         description=input("Enter description:")
#         amount=input("Enter amount:")
#         with open(filename,"a",newline="") as f:
#             writer=csv.writer(f)
#             writer.writerow([date, description, amount])
#         print("Expense added!")
#     elif choice=="2":
#         try:
#             with open(filename,"r") as f:
#                 reader=csv.reader(f)
#                 next(reader)
#                 print("\nYour Expenses:")
#                 for row in reader:
#                     print(f"- Date: {row[0]}, Description: {row[1]}, Amount: Rs.{row[2]}")
#         except FileNotFoundError:
#             print("No expenses found. Please add an expense first.")
#     elif choice=="3":
#         print("Exiting Expense Tracker. Goodbye!")
#         break
#     else:
#         print("Invalid choice, try again.")
            
# import csv 
# import os 

# filename="expanses.csv"

# if not os.path.exists(filename):
#     with open(filename,"w",newline="")as f:
#      writer = csv.writer(f)
#      writer.writerow(["date", "Description", "Expance"])
#     print("file Successfully Created")
# while True:
#     print("----welcome to Expanse manager---")
#     print("1.Add Expanse:")
#     print("2. View Expanse:")
#     print("3. Exit Expance book")
    
#     choice=input('Enter you choice from (1-4)')
    
#     if choice=="1":
#         date=input("Enter date in (yyyy-mm-dd")
#         description=input("Enter Description")
#         expanse=input("Enter Expanse")
#         with open(filename,"a",newline="") as f:
#             writer=csv.writer(f)
#             writer.writerow([date,description,expanse])
#         print("Expanse Added Successfully")
#     elif choice=="2":
#         try:
#             with open(filename,"r") as f:
#                 reader=csv.reader(f)
#                 next(reader)
#                 print("\nYour Expanse:")
#                 for row in reader:
#                     print(f"- Date: {row[0]}, Description: {row[1]}, Amount: Rs.{row[2]}")
#         except FileNotFoundError:
#             print("No expenses found. Please add an expense first.")
                   
# import pandas as pd
# import os

# filename = "expenses.csv"

# # Create CSV file if not exists
# if not os.path.exists(filename):
#     df = pd.DataFrame(columns=["Date", "Description", "Amount"])
#     df.to_csv(filename, index=False)
#     print("CSV file created successfully!")

# while True:
#     print("\n--- Expense Tracker Menu ---")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Show Total Expenses")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         date = input("Enter date (yyyy-mm-dd): ")
#         description = input("Enter description: ")
#         amount = float(input("Enter amount: "))

#         # Load existing CSV
#         df = pd.read_csv(filename)

#         # Append new row
#         new_row = {"Date": date, "Description": description, "Amount": amount}
#         df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#         # Save back to CSV
#         df.to_csv(filename, index=False)
#         print("Expense added!")

#     elif choice == "2":
#         df = pd.read_csv(filename)
#         print("\n--- Your Expenses ---")
#         print(df)

#     elif choice == "3":
#         df = pd.read_csv(filename)
#         total = df["Amount"].sum()
#         print(f"\n💰 Total Expenses: {total}")

#     elif choice == "4":
#         print("Exiting... Goodbye!")
#         break

#     else:
#         print("Invalid choice! Try again.")                 
import pandas as pd
# Load the CSV file
df = pd.read_csv("expenses.csv")
# Show the entire DataFrame
print(df)
# Show first 5 rows only
print("\n--- First 5 rows ---")
print(df.head())
# Show last 5 rows only
print("\n--- Last 5 rows ---")
print(df.tail())
# Show some quick info about columns
print("\n--- Info ---")
print(df.info())

# Show basic statistics (only works for numeric columns like Amount)
print("\n--- Statistics ---")
print(df.describe())
