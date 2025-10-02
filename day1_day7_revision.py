name = "Asad"
age = 23

print (f"My name is {name} and my age is {age}")

#################################

a=input("Enter a value to print its table on the console:")
a=int(a)

for i in range(1,11):
 
    print(f"{a}x{i}={a*i}")
    
####################################
if a>18:
    print("you are eligibal for Vote")
elif a<18:
    print("you are not eligibal for vote")
else:
    print("you are just eligibal for vote")
###########################################

b=input("Enter the value of b:")
b=int(b)
if a>b:
    print(f"a is greater than b")
print (a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print((a+b)/2)
print(max(a,b))
print(min(a,b))
print(abs(a))
print(abs(b))
print(int(a**0.5))
print(float(a))
print(complex(a))
print(round(3.7))
print(round(3.4))
print(pow(a,b))
print(bin(a))
print(oct(a))
print(hex(a))
print(str(a))
print(bool(a))
print(bool(0))
print(bool(-1))
print(bool(""))
print(chr(56))
print(ord('8'))
##########################################
fruits=["apple","banana","orange","grapes","mango"]
print(fruits)
print(fruits[0])
print(fruits[1])
fruits.append("kiwi")
fruits.insert(1, "watermelon")
fruits.remove("banana")
print(fruits[0:4])
for i in fruits:
    print(i)
##########################################
# Shopping Cart Program


cart=[]

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")
    
    choice =input("Enter your choice (1-4): ")
    
    if choice=="1":
        item=input("Enter item to add:")
        cart.append(item)
        print(f"{item} added to cart.")
    elif choice=="2":
        item=input("Enter item to remove:")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from cart.")
        else:
            print("Item not found in cart.")
    elif choice=="3":
        print("\nYour Cart Items:")
        if len(cart)==0:
            print("Cart is empty.")
        else:
            for i in cart:
                print(i)
    elif choice=="4":
        print("Exiting Shopping Cart. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
####################################################
student={
    "name":'Asad',
    "age":23,
    "courses":["Math","CompSci"],
    "is_active":True
}
student["age"]=24
student["phone"]="1234567890"
print(student)
for key,value in student.items():
    print(f"{key}:{value}")
#######################################
pro_tuple=("apple","banana","orange","grapes","mango")

print(pro_tuple)
print(pro_tuple[0])
print(pro_tuple[1])
###############################################
#file handling

with open("asad.txt","w") as f:
    f.write("Hello Asad\n")
    f.write("This is your first file handling program.\n")
    f.write("You are doing great!\n")
    print("File created and data written successfully!")
with open("asad.txt","r") as f:
    content=f.read()
    print(content)
#################################
try:
    with open("asad.text","r") as f:
        content=f.read()
    print(content)
except FileNotFoundError:
    print("❌ File not found! Please check filename.")
###############################
import csv
import os
filename="expanditures.csv"


if not os.path.exists(filename):
    with open(filename,"w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow(["Date","Description","Amount"])
    print("CSV file created successfully!")
#######################################################
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
print(add(5,5))
print(subtract(10,5))
#########################################
class Student:
    def car():
        print("This is a car")
    def bike():
        print("This is a bike")
st = Student()
st.car()
st.bike()
###########################################
        
        