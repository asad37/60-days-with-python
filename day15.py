#file handling
class Student:
    def __init__(self, name, age, grade):
        self.name = name           # public
        self._age = age            # protected
        self.__grade = grade       # private

    def show_info(self):
        print(f"Name: {self.name}")      # Public access
        print(f"Age: {self._age}")       # Protected access
        print(f"Grade: {self.__grade}")  # Private access

    # Getter for private variable
    def get_grade(self):
        return self.__grade

    # Setter for private variable
    def set_grade(self, grade):
        self.__grade = grade


# Create object
student1 = Student("Asad", 22, "A")

# Accessing public
print(student1.name)    # ✅ Works fine

# Accessing protected
print(student1._age)    # ⚠️ Works, but not recommended outside class

# Accessing private directly
# print(student1.__grade) ❌ Error

# Accessing private using getter
print(student1.get_grade())  # ✅ Works

# Updating private using setter
student1.set_grade("A+")
print(student1.get_grade())  # ✅ Updated
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number   # public
        self.__balance = balance               # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# Test
acc1 = BankAccount("123456", 5000)
print(acc1.account_number)   # ✅ Accessible
# print(acc1.__balance) ❌ Error (Private)

acc1.deposit(2000)
acc1.withdraw(1000)
print("Current Balance:", acc1.get_balance())
