#Advance functions and file handling
import math
from functools import reduce
import random
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
print(math.pow(2,3))
print(math.log(100,10))
print(math.sin(90))
print(math.cos(0))
print(math.tan(45))
print(math.ceil(4.2))
print(math.floor(4.7))
print(math.gcd(12,15))
print(math.lcm(12,15))
print(math.radians(90))
print(math.degrees(math.pi/2))
print(math.isqrt(20))
print(math.copysign(5,-3))
print(math.fabs(-7))
print(math.modf(5.67))
print(math.log10)
print(math.expm1(1))
print(math.erf(1))
#################################################3
f = open("demo.txt", "w")
f.write("Hello, Asad!\nWelcome to Python Day 10.")
print("File created and data written successfully.")
f.close()


f=open("asad.txt","w")
f.write("Hello Asad!\nWelcome to Python Day 10.")
print("File created and data written successfully.")
f.close()


f=open("demo.txt","r")
print(f.read())
f.close()

even_number=lambda x:x%2==0
print(even_number(4))

cube_number=lambda x:x*x*x
print(cube_number(3))

map_numbers=[1, 2, 3, 4, 5]
squared_numbers=list(map(lambda x:x*x,map_numbers))
print(squared_numbers)

filter_numbers=[10, 15, 20, 25, 30]
filtered_numbers=list(filter(lambda x:x%2!=0,filter_numbers))
print(filtered_numbers)

reduce_numbers=[5, 10, 15, 20]
product=reduce(lambda a,b:a*b,reduce_numbers)
print(product)


import math
print(math.sqrt(81))
print(math.sin(90))
print(math.pi)


print(random.randint(1,100))
list_friuts=["apple","banana","cherry","date"]
print(random.choice(list_friuts))
random.shuffle(list_friuts)
print(list_friuts)



f=open("notes.txt","w")
f.write("Python is very easy to learn and i enjoy a lot with python programing and i am very happy to learn python")
f.close()
f=open("notes.txt","r")
print(f.read())
f.close()
###################
#Appent note in file
f=open("notes.txt","a")
f.write("\nI will master Python step by step!")