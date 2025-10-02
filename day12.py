class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def info_detail(self):
        print(f"Car Brand is {self.brand}")
        print(f"Car model is {self.model}")
        print(f"car year is {self.year}")
car1=Car("Honda","City",2025)
car2=Car("Honda","Civic",2023)

car_list=[car1,car2]
for car in car_list:
    car.info_detail()