class vehicle:
    def __init__(self,brand,year):

        self.brand = brand
        self.year = year

    def display_info(self):
        print(f" vehicle {self.brand} for {self.year}")

class car(vehicle):
    def __init__(self, brand, year,num_door):
        super().__init__(brand, year)
        self.num_door = num_door

    def display_info(self):
        print(super().display_info)
        print(f"machine {self.brand} for {self.year} and have {self.num_door} door")

class motor(vehicle):
    def __init__(self, brand, year,has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
    def display_info(self):
        print(super().display_info)
        print(f"motor {self.brand} for {self.year} and {self.has_sidecar}")


v = vehicle(input("enter the brand of youre vehicle : "),int(input("enter the year of your vehicle :")))
c = car(input("enter the brand of youre car : "),int(input("enter the year of your car :")),int(input("enter the number of yure cars door :")))
m = motor(input("enter the brand of youre motor : "),int(input("enter the year of your motor :"))," no ")

v.display_info()
c.display_info()
m.display_info()



        