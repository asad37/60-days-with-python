#Part 1 Q#1
x = 5
y = 3
print(x ** y)
#the result of the above program is 125
'''
Question#02
the difference b/w = and == is the = is used to assign value to the variable for example x=2 and the == is used to compare two values for example if x==0: print("x is equal to zero")
'''
######################
for i in range(1,11):
    print(i)
#########################
#part-02 Question No:01
def add(a, b=2):
    return a + b

print(add(3))
print(add(3, 4))
#the output of the program will be first=5 and second=7

#question No#02

def multiply(a,b):
    return a*b
print(multiply(12,45))


#Part 3 Question no#01

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
#the print result will be ["apple","banana","cherry","orange"]

student={
    "name":"Asad",
    "age":23,
    "city":"Kasur"
}
print(f"My age is:{student["age"]}")

###############################3
#part 4
#class is a blueprint in python blueprint mean it not have any memory and the empty jar which have multiple methods and function which make it meaningful for example in python class Car:
#The __init__ method is called a Constructor in Python classes.

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def show_details(self):
        print(f"Student name is: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student Obtained marks are: {self.marks}")
        if self.marks>=50 and self.marks<=59:
            print(f"Student get D grade")
        elif self.marks>60 and self.marks<=70:
            print("Student grade is C")
        elif self.marks<50:
            print("Student is fail")
        elif self.marks>90 and self.marks<=100:
            print("Student Get A+ Grade")
        else:
            print("Invalid Marks")
std1=Student("Asad",23,93)
std1.show_details() 
#class is a blueprint which have methods and functions and the method is a piece of code which perform a spacific task it have memory and class does not have any memory
#if we have vehicle class and car class inherit from it so according to inheritence the vehicle class is called parent class and car class is called child class class Vehicle: and car class Car(Whicle):
#we use __ double under score in encapsulation because in encapsulation we deal with sensitive information and keep the variable private by using the __ double underscore for exapmple in bankaccount case the __balance will be private variable that can not be accessed outside the class 