# fruits=["Apple","Banana","Mango","Grapes"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])

# for i in fruits:
#     print(i)
    
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(sorted(numbers,reverse=True))
# print(numbers)
# print(numbers[2:5])


# movies=["3 idiots","PK","Dangal","Lagaan","Sholay"]
# print(movies)
# movies.append("Bahubali")
# print(movies)
# movies.insert(1,"RRR")
# print(movies)
# movies.remove("Lagaan")
# print(movies)
# print(movies[0:4])
# for i in movies:
#     print(i)
# Shopping Cart Program

# cart = []  # empty list for storing items

# while True:
#     print("\n--- Shopping Cart Menu ---")
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. View cart")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         item = input("Enter item to add: ")
#         cart.append(item)
#         print(f"{item} added to cart.")

#     elif choice == "2":
#         item = input("Enter item to remove: ")
#         if item in cart:
#             cart.remove(item)
#             print(f"{item} removed from cart.")
#         else:
#             print("Item not found in cart.")

#     elif choice == "3":
#         print("\nYour Cart Items:")
#         if len(cart) == 0:
#             print("Cart is empty.")
#         else:
#             for i in cart:
#                 print("-", i)

#     elif choice == "4":
#         print("Exiting... Thank you for shopping!")
#         break

#     else:
#         print("Invalid choice! Please try again.")
# ##############################################33


# cart =[]

# while True:
#     print("\n--- Shopping Cart Menu ---")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. View Cart")
#     print("4. Exit")
    
#     choice = input("Enter your choice (1-4): ")
    
#     if choice == "1":
#         item =input ("Enter item to add:")
#         cart.append(item)
#         print(f"{item} added to cart.")
#     elif choice == "2":
#         item =input("Enter item to remove:")
#         cart.remove(item)
#         print(f"{item} removed from cart.")
#     elif choice == "3":
#         print("\nYour Cart Items:")
#         if len(cart)==0:
#             print("Cart is empty.")
#         else:
#             for i in cart:
#                 print("-",i)
#     elif choice == "4":
#         print("Exiting... Thank you for shopping!")
#         break
#     else:
#         print("Invalid choice! Please try again.")
# Store items with prices
# Store items with prices
import random
from datetime import datetime

# Store items with prices
store = {
    "Milk": 50,
    "Bread": 30,
    "Eggs": 10,
    "Rice": 200,
    "Chicken": 500,
    "Apple": 100
}

cart = {}  # item -> quantity

while True:
    print("\n------ Welcome to Shopping Cart ------")
    print("1. View Store Items")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart & Total Bill")
    print("5. Checkout & Exit")
    
    choice = input("Enter your Choice (1-5): ")
    
    if choice == "1":
        print("\nAvailable Items in Store:")
        for item, price in store.items():
            print(f"- {item} : Rs.{price}")

    elif choice == "2":
        item = input("Enter Item name to add in cart: ")
        if item in store:
            qty = int(input(f"Enter quantity of {item}: "))
            if item in cart:
                cart[item] += qty   # add more quantity
            else:
                cart[item] = qty
            print(f"{qty} x {item} added to cart")
        else:
            print("Item not available in store")

    elif choice == "3":
        item = input("Enter Item name to remove from cart: ")
        if item in cart:
            qty = int(input(f"Enter quantity of {item} to remove: "))
            if qty >= cart[item]:
                del cart[item]  # remove completely
                print(f"{item} removed from cart")
            else:
                cart[item] -= qty
                print(f"{qty} x {item} removed from cart")
        else:
            print("Item not found in cart")

    elif choice == "4":
        if not cart:
            print("Cart is empty")
        else:
            print("\nYour Cart Items:")
            total = 0
            for item, qty in cart.items():
                price = store[item] * qty
                print(f"- {item} (x{qty}) : Rs.{price}")
                total += price

            # Apply discount 🎁
            discount = 0
            if total >= 1000:
                discount = total * 0.1  # 10% discount
                print(f"\n🎁 Congratulations! You got a 10% discount: Rs.{discount}")

            grand_total = total - discount
            print(f"Total Bill = Rs.{grand_total}")

    elif choice == "5":
        if not cart:
            print("Cart is empty. Nothing to checkout.")
        else:
            # Generate Invoice 🧾
            invoice_no = random.randint(1000, 9999)
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("\n------ 🧾 INVOICE ------")
            print(f"Invoice No: {invoice_no}")
            print(f"Date: {date_time}")
            print("\nItems Purchased:")

            total = 0
            for item, qty in cart.items():
                price = store[item] * qty
                print(f"- {item} (x{qty}) : Rs.{price}")
                total += price

            discount = 0
            if total >= 1000:
                discount = total * 0.1
                print(f"\n🎁 Discount Applied: Rs.{discount}")

            grand_total = total - discount
            print(f"\nFinal Amount to Pay = Rs.{grand_total}")
            print("\nThank you for shopping with us 🙌")

        break

    else:
        print("Invalid choice! Please Try Again.")
