# Day 7 (Functions Basics)

# Q1: Write a function greet_user(name) that prints "Hello <name>".

# def greet_user(name):
#     print(f"Hello {name}")

# greet_user("Asad")


# Q2: Difference between return and print?

# return → sends value back from function (can be used later).

# print → only shows value on screen, cannot reuse it.

# 🔹 Day 8 (Classes & Objects Basics)

# Q3: Class Book

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# book1 = Book("Python 101", "Mark")
# book2 = Book("OOP in Python", "John")

# print(book1.title, "-", book1.author)
# print(book2.title, "-", book2.author)


# Q4: __init__ is the constructor, runs automatically when object is created, and initializes attributes.

# 🔹 Day 9 (Methods in Class)

# Q5: Add display_info()

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def display_info(self):
#         print(f"Book: {self.title}, Author: {self.author}")

# book = Book("Python Mastery", "Asad")
# book.display_info()


# Q6:

# Instance method → Works with object (self).

# Class method → Works with class itself (@classmethod, cls).

# 🔹 Day 10 (Constructors & Multiple Objects)

# Q7 & Q8:

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def info_detail(self):
#         print(f"{self.brand} {self.model}, Year: {self.year}")

# car1 = Car("Honda", "City", 2025)
# car2 = Car("Toyota", "Corolla", 2024)

# cars = [car1, car2]
# for c in cars:
#     c.info_detail()

# 🔹 Day 11 (Inheritance Basics)

# Q9:

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")

# class Cat(Animal):
#     def speak(self):
#         print("Meow")

# animals = [Animal(), Dog(), Cat()]
# for a in animals:
#     a.speak()


# Q10: Advantage → Code reusability (child inherits parent’s properties).

# 🔹 Day 12 (Polymorphism)

# Q11: Polymorphism → Same method name but different behavior.

# print(len("Hello"))   # Works on string
# print(len([1,2,3]))   # Works on list


# Q12: Shape Example

# class Shape:
#     def cal_Area(self):
#         pass

# class Square(Shape):
#     def cal_Area(self):
#         return 2 * 2

# class Rectangle(Shape):
#     def cal_Area(self):
#         return 2 * 4

# shapes = [Square(), Rectangle()]
# for s in shapes:
#     print(s.cal_Area())

# 🔹 Day 13 (Method Overriding)

# Q13: Method overriding → Child class provides new definition of a method that exists in parent.

# Q14:

# class Animal:
#     def speak(self): print("Animal sound")

# class Dog(Animal):
#     def speak(self): print("Bark")

# class Cat(Animal):
#     def speak(self): print("Meow")

# for a in [Animal(), Dog(), Cat()]:
#     a.speak()

# 🔹 Day 14 (Abstraction)

# Q15: Abstraction → Hiding implementation, only showing what’s necessary.

# Q16: Abstract class example:

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self): pass
    
#     @abstractmethod
#     def perimeter(self): pass

# class Circle(Shape):
#     def __init__(self, r): self.r = r
#     def area(self): return 3.14 * self.r * self.r
#     def perimeter(self): return 2 * 3.14 * self.r

# 🔹 Day 15 (Encapsulation)

# Q17: Encapsulation → Restricting direct access to data, using getters/setters.

# Q18: BankAccount Example

# class BankAccount:
#     def __init__(self, acc_no, balance=0):
#         self.account_number = acc_no
#         self.__balance = balance  # private variable
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")
    
#     def get_balance(self):
#         return self.__balance

# acc = BankAccount("12345", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print(acc.get_balance())   # 1300


# 🔥 Bonus: Abstraction vs Encapsulation

# Abstraction → Hides implementation details (what to do, not how).

# Encapsulation → Hides data (keeping variables private).