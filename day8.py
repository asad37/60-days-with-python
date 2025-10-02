#Day 8 OOP Basics in Python 
# Classes and Objects
# A class is like a blueprint for creating objects. An object has properties and behaviors associated with it. In Python, we use the class keyword to define a class.
# class Dog:
#     # Class Attributes
#     species = "Canis familiaris"


# 1. What is a Class & Object?

# Class = blueprint (like a design for a car 🚗).

# Object = actual instance created from that class (a real car made from that design).


# class Car:
#     def addNumbers(a,b):
#         print("My name is Asad Waqas",a+b)
#     def subtract(a,b):
#         print(a-b)
# Car.addNumbers(1,3)
# Car.subtract(23,45)


####################################3
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def show_details(self):
#         print(f"Car:{self.brand} {self.model}")
# car=Car("Honda","Civic")
# car.show_details()


class Animals:
    def speek(self):
        print("This is an animal")
class Dog(Animals):
    def speek(self):
        print("Bow Bow")
class Cat(Animals):
    def speek(self):
        print("Meow")
d=Dog()
c=Cat()
an=Animals()
an.speek()
c.speek()
d.speek()