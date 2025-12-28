class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"the vehicle is {self.brand} and has {self.year} yers old")

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors
    def display_info(self):
        print(f"this car has {self.num_doors} doors")
        return super().display_info()
    
class Motor(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar =has_sidecar
    def display_info(self):
        if(self.has_sidecar=="True"):
            print("Yes")
        else:
            print("No")
        return super().display_info()
    
v =Vehicle("benz" , 20)
c =Car("BMW", 25, 4)
m= Motor("apachi", 10, False)

v.display_info()
c.display_info()
m.display_info()    
    