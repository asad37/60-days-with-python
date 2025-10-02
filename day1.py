import math

# name="Asad Waqas"
# age=23
# country="Pakistan"
# job="Software Engineer"
# profession="Application Developer"
# fav_programing_language="Python"
# fav_backend_framework="Django"
# fav_frontend_framework="React"
# print(f"My name is {name}. I am {age} years old from {country}. I work as a {job} and my profession is {profession}. My favorite programming language is {fav_programing_language}. My favorite backend framework is {fav_backend_framework} and my favorite frontend framework is {fav_frontend_framework}.")

a=input("Enter value of a: ")
b=input("Enter value of b: ")
a=int(a)
b=int(b)
print("The sum of a and b is:",a+b)
print("The difference of a and b is:",a-b)
print("The product of a and b is:",a*b)
print("The division of a and b is:",a/b)
print("The modulus of a and b is:",a%b)
print("The floor division of a and b is:",a//b)
print("The exponent of a and b is:",a**b)
print("The average of a and b is:",(a+b)/2)
print("The maximum of a and b is:",max(a,b))
print("The minimum of a and b is:",min(a,b))
print("The absolute value of a is:",abs(a))
print("The absolute value of b is:",abs(b))
print("The square root of a is:",math.sqrt(a))
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")
    
##################################
if a % 2 == 0 and b % 2 == 0:
    print("Both a and b are even")
elif a % 2 == 0 and b % 2 != 0:
    print("a is even, b is odd")
elif a % 2 != 0 and b % 2 == 0:
    print("a is odd, b is even")
else:
    print("Both a and b are odd")
##################################
if (a+b)%5==0:
    print("The sum of a and b is divisible by 5")
else:
    print("The sum of a and b is not divisible by 5")
##################################
if (a*b)%3==0 and (a*b)%7==0:
    print("The product of a and b is divisible by both 3 and 7")
elif (a*b)%3==0 and (a*b)%7!=0:
    print("The product of a and b is divisible by 3 but not by 7")
elif (a*b)%3!=0 and (a*b)%7==0:
    print("The product of a and b is divisible by 7 but not by 3")
else:
    print("The product of a and b is not divisible by both 3 and 7")
#######3###########################
# Check if the sum, difference, and product of a and b are all divisible by 5.

# Print a message for each case separately.
if a+b % 5==0:
    print("The sum of a and b is divisible by 5")
elif a-b % 5==0:
    print("The difference of a and b is divisible by 5")
elif a*b % 5==0:
    print("The product of a and b is divisible by 5")
elif a+b % 5==0 and a-b % 5==0:
    print("The sum and difference of a and b are divisible by 5")
elif a+b % 5==0 and a*b % 5==0:
    print("The sum and product of a and b are divisible by 5")
elif a-b % 5==0 and a*b % 5==0:
    print("The difference and product of a and b are divisible by 5")
elif a+b % 5==0 and a-b % 5==0 and a*b % 5==0:
    print("The sum, difference, and product of a and b are all divisible by 5")
else:
    print("The sum, difference, and product of a and b are not divisible by 5")
    