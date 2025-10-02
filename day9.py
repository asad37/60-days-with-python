from functools import reduce

# def greet(name="Guest"):
#     print(f"Hello {name}: Welcome to Day 9!")
# greet("Alice")
# greet()

# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(10,23,45,56,78,90))


# def std_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# std_info(name="John", age=21, course="B.Tech")





# square=lambda x:x*x
# addition=lambda a,b:a+b
# print(square(5))
# print(addition(10,20))




# def cal_area(radius,pi=3.14):
#     return pi*radius*radius
# print(cal_area(5))
# print(cal_area(7,3.1416))


# def mul_nums(*args):
#     result=1
#     for num in args:
#         result*=num
#     return result
# print(mul_nums(2,3,4))


# numbers = [10, 20, 55, 60, 70, 25, 90, 30]
# greater_50 = list(filter(lambda x: x > 50, numbers))
# print("Numbers greater than 50:", greater_50)


# nums2 = [2, 3, 4, 5]
# product = reduce(lambda a, b: a * b, nums2)
# print("Product of numbers [2,3,4,5]:", product)



# map_numbers=[1,3,56,78,7]
# squar_numbers=list(map(lambda x:x*x,map_numbers))
# print(squar_numbers)

# reduce_nums=reduce(lambda a,b:a*b,map_numbers)
# print(reduce_nums)

