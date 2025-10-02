#Object Oriented Programing
# class Car:
#     def __init__(self,make,model,year):
#         self.model=model
#         self.make=make
#         self.year=year
#         self.odometer_reading=0
#     def show_detail(self):
#         print(f"Car Make: {self.make}")
#         print(f"Car Model: {self.model}")
#         print(f"Car Year: {self.year}")
#         print(f"Odometer Reading: {self.odometer_reading} km")
# car1=Car("Toyota","Corolla",2020)
# car2=Car("Honda","Civic",2019)
# car3=Car("Ford","Mustang",2021)
# car4=Car("Chevrolet","Camaro",2018)
# car5=Car("BMW","3 Series",2022)
# car6=Car("Audi","A4",2021)
# car7=Car("Mercedes-Benz","C-Class",2020)
# car8=Car("Volkswagen","Golf",2019)
# car9=Car("Hyundai","Elantra",2022)
# car10=Car("Nissan","Altima",2021)
# car1.odometer_reading=15000
# car_list=[car1,car2,car3,car4,car5,car6,car7,car8,car9,car10]
# for car in car_list:
#     car.show_detail()
    
# ##############################################3


# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#     def show_detail(self):
#         print(f"Vehicle Brand: {self.brand}")
# class Bike(Vehicle):
#     def __init__(self,brand,cc):
#         super().__init__(brand)
#         self.cc=cc
#     def show_detail(self):
#         super().show_detail()
#         print(f"Bike Capacity: {self.cc}")
        
# bike1=Bike("Yamaha","125")
# bike1.show_detail()


# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance   # private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance for Withdrawal!")

#     def get_balance(self):
#         return self.__balance

# acc = Account("Asad", 5000)
# acc.deposit(2000)
# acc.withdraw(8000)
# print("Present Balance:", acc.get_balance())



# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self._balance=balance
#     def deposit(self,amount):
#         self._balance+=amount
#     def withdraw(self,amount):
#         if amount<=self._balance:
#             self._balance-=amount
#         else:
#             print("Insufficient Balance for Withdrawal!")
#     def get_balance(self):
#         return self._balance
# account=BankAccount("Asad",5000)
# account.deposit(2000)
# account.withdraw(8000)
# print("Present Balance:",account.get_balance())



##############################################################
class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
    def calculate_grade(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=80:
            return 'B'
        elif self.marks>=70:
            return 'C'
        elif self.marks>=60:
            return 'D'
        else:
            return 'F'
student1=Student("Asad",101,85)
student2=Student("Ali",102,92)
student3=Student("Ahsan",103,76)
list_students=[student1,student2,student3]
for student in list_students:
    student.display_info()
    print(f"Grade: {student.calculate_grade()}")
    print("#########################")
##########################################################
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
    def withdrawel(self,amount):
        if amount<=self._balance:
            self._balance-=amount
        else:
            print("Insufficient Balance for Withdrawel!")
    def get_balance(self):
        return self._balance
account=Account("Asad",5000)
account.deposit(2000)
account.withdrawel(8000)
print("Present Balance:",account.get_balance())

###########################################################
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
animals=[Dog(),Cat()]
for animal in animals:
    animal.sound()
