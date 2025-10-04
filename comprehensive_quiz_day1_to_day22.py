#1.	Print "Hello Python".
print("Hello Python")
#2.	Swap two numbers.
a=5
b=10
temp=a
a=b
b=temp
print("a=",a, "b=",b)
#3.	Check if a number is even or odd.
number=input("Enter a number to check even or odd:")
number=int(number)
if number%2==0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
#4.	Find factorial of a number.
import math
print(math.factorial(number))
#5.	Generate Fibonacci sequence up to n terms.
a,b=0,1
count=0
if number<0:
    print("n is less than 0 Enter a valid number")
elif number==1:
    print("fabonicci Sequence",a)
else:
    print("Fabonacci Sequence")
    while count<number:
        print(a,end=" ")
        a,b=b,a+b
        count+=1
#6.	Reverse a string.
text="Hello World"
reversed_text=text[::-1]
print(f"\n{reversed_text}")
#7.	Count vowels in a string.
vowels="aeiouAEIOU"
for char in text:
    if char in vowels:
        count+=1
print(f"Number of Vowels:{count}")
#8.	Find max of three numbers.
a,b,c=40,2,3
if a>b and a>c:
    print("A is tha largest number")
elif b>a and b>c:
    print("b is the largest number")
else:
    print("c is the largest number")
#9.	Print multiplication table of 5.
for i in range(1,11):
    print(f"{i}x5={i*5}")
#10.	Check if a number is prime.
if number>0:
    for i in range(2,number):
        if number%i==0:
            print(number," is not a prime number")
            break
        else:
            print(number," is a prime number")
else:
    print(number," is not a prime number")
#11.	Write a function to check if a string is palindrome.
def is_palindrome(text):
    text=text.replace(" ","").lower()
    return text==text[::-1]
s=input("Enter a string:")
if is_palindrome(s):
    print("Palindrom")
else:
    print("Not a palindrome")
#12.	Write a function to calculate area of a circle.
def area_circle(radius):
    area=3.1416*radius*radius
    print(f"The area of circle is: ",area)
area_circle(34)
#13.	Write a function to find sum of digits.
def sum_ofdigit():
    a,b=12,45
    print(f"The sum of String is: ",(a+b))
sum_ofdigit()
#14.	Write a recursive factorial function.

def fact_num(number):
    if number==0 or number==1:
        return 1
    else:
        return number*fact_num(number-1)
print("factoriial of ",number, "is: ",fact_num(number))
#15.	Write a function that returns n-th Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)   # recursive call

# Example usage
num = int(input("Enter n: "))
print(f"{num}-th Fibonacci number is:", fibonacci(num))
#16.	Create a class Car with attributes brand & model.
#17.	Add a method display() in Car to print info.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Car Brand is ",self.brand,"and model is ",self.model)
       
car1=Car("Honda","City")
car1.display()
#18.	Create a class BankAccount with deposit & withdraw.
class BankAccount:
    def __init__(self,owner,_balance):
        self.owner=owner
        self._balance=_balance
    def deposit(self,amount):
        if amount>0:
            self._balance += amount
            print(f"{amount}-\PKR successfully Deposited in your Account")
        elif amount==0:
            print("you Enter 0 which is not an amount")
        else:
            print("Invalid Ammount")
    def withdrwal(self,amount):
        if amount<self._balance:
            self._balance-=amount
            print(f"{amount}-\PKR successfully withdraw from your Account")
        elif amount>self._balance:
            print("Insufficient Balance to withdraw")
        else:
            print("invalid entry")
    def current_balance(self):
        print(f"Your Current Balance is {self._balance}-\PKR")
acc=BankAccount("Asad",1000)
acc.deposit(12000)
acc.withdrwal(4000)
acc.current_balance()
#19.	Demonstrate inheritance with class Animal → Dog.
class Animal:
    def sound(self):
        print("Voices of Animals")
class Dog(Animal):
    def sound(self):
        print("Dog Speek Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Cat sound is meow meow")
ani_list=[Animal(),Dog(),Cat()]
for i in ani_list:
    i.sound()
#20.	Demonstrate polymorphism with a method speak() in different classes.
class Animal:
    def sound(self):
        print("Voices of Animals")
class Dog(Animal):
    def sound(self):
        print("Dog Speek Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Cat sound is meow meow")
ani_list=[Animal(),Dog(),Cat()]
for i in ani_list:
    i.sound()
#21.	Write a program to read a text file.
with open("asad.txt","r")as file:
    print(file.read())
#22.	Write a program to append to a file.
with open("asad.txt","a")as file:
    file.write("\n Asad Waqas can come to university")
#23.	Write a program to count words in a file.
with open("asad.txt","r")as file:
    content=file.read()
    words=content.split()
    print(f"The words in the file asad.txt are:",len(words))
#25.	Write a program to handle FileNotFoundError.
try:
    with open("waqas.txt","r")as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("Sorry file is not found")
#26.Write code that raises a ValueError if input < 0.
n=input("Enter a number")
n=int(n)
if n<=0:
    raise ValueError ("n is less than the 0")
else:
    print("Valid input",n)
#27 Use try-except to catch ZeroDivisionError.
try:
    result=2/n
except ZeroDivisionError:
    print("Error:There is a zerodivision error in the code")
finally:
    print("Finally Execution Complete")
#28.Write a program with finally block.
try:
    result=2/n
except ZeroDivisionError:
    print("Error:There is a zerodivision error in the code")
finally:
    print("Finally Execution Complete")
#29.Create a custom exception class.

    

    