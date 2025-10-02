#Abstraction in programing is the hiding implimentation detail from detail from user 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    
    def area(self):
        pass
    def perameter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perameter(self):
        return 2*(self.length*self.width)
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
    def perameter(self):
        return self.length+self.length+self.length+self.length
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.1416*(self.radius*self.radius)   
    def perameter(self):
        return 2*3.1416*self.radius
shapes=[Square(7),Rectangle(6,7),Circle(7)]
for i in shapes:
    print(f"The area of the shape is {i.area()}")
    print(f"The Perameter is {i.perameter()}") 
    print("__---------------------------__")   
    