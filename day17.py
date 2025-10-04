# # Exception Handling in Python
# # try:
# #     x=int("ABC")
# # except ValueError:
# #     print("Cannot convert into int")
# # try:
# #     x=10/0
# # except ZeroDivisionError:
# #     print("Zero can never devide the 10")
# # except ValueError:
# #     print("Invalid value input")
# # try:   
# #     f=open("text.txt","r")
# #     print(f.read())
# # except FileNotFoundError:
# #     print("File not Found")
# # finally:
# #     print("Failed to fetch the file")

# # def check_age(age):
# #     if age < 18:
# #         raise ValueError("Age must be 18 or above")
# #     else:
# #         print("Valid age:", age)

# # try:
# #     check_age(15)
# # except ValueError as e:
# #     print("Error:", e)

# def c_age(age):
#     if age<18:
#         raise ValueError ("Age is less than 18")
#     else:
#         print("Valid Age")
# try:
#     c_age(15)
# except ValueError as e:
#     print("Error",e)
    
# ✅ Q6. File Handling with Exception

# 👉 Requirement: Open data.txt, read content if exists, else print "File not found!".

# try:
#     with open("data.txt", "r") as file:
#         content = file.read()
#         print("File Content:\n", content)
# except FileNotFoundError:
#     print("File not found!")


# 🔎 Explanation:

# with open() ensures file closes automatically.

# FileNotFoundError handles the case when file doesn’t exist.

# ✅ Q7. Divide Function with Exception

# 👉 Requirement: Divide two numbers, raise error if denominator = 0.

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return a / b

# try:
#     print(divide(10, 2))   # ✅ Works fine
#     print(divide(5, 0))    # ❌ Raises error
# except ZeroDivisionError as e:
#     print(e)


# 🔎 Explanation:

# raise ZeroDivisionError("message") creates a custom error.

# We handle it in a try-except.

# ✅ Q8. Age Validation Function

# 👉 Requirement: Raise error if age < 18, else print "Valid Age".

# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be at least 18")
#     else:
#         print("Valid Age")

# try:
#     check_age(20)   # ✅ Valid
#     check_age(15)   # ❌ Raises error
# except ValueError as e:
#     print(e)


# 🔎 Explanation:

# raise ValueError is used to signal invalid input.

# If age >= 18, program continues normally.
    
