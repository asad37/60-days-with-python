# class Animals:
#     def speak(self):
#         print("Animals Sound")
# class Dog(Animals):
#     def speak(self):
#         print("Dog Barks")
# class Cat(Animals):
#     def speak(self):
#         print("Cat MeoMeo")
# class Gay(Animals):
#     def speak(self):
#         print("Gaa Gaa")
# ani_list=[Animals(),Dog(),Cat(),Gay()]
# for i in ani_list:
#     i.speak()
class Shape:
    def cal_Area(self):
        print("Calculate Area of the shape")
class Square(Shape):
    def cal_Area(self):
        height=2
        width=2
        area=height*width
        print(f"Area of Square is: {area}")
class Rectangle(Shape):
    def cal_Area(self):
        height=2
        width=4
        area=height*width
        print(f"Area of Rectangle is: {area}")
area_shape=[Shape(),Square(),Rectangle()]
for i in area_shape:
    i.cal_Area()