# Parent class
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def display_info(self):
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} kmpl")


# Child class Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, max_speed, mileage, brand):
        # Call parent constructor using super()
        super().__init__(max_speed, mileage)
        self.brand = brand
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        super().display_info()


# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity
    
    def display_info(self):
        print(f"Bus Capacity: {self.capacity} passengers")
        super().display_info()


# Example usage
car1 = Car(200, 18, "Toyota")
bus1 = Bus(120, 8, 50)

car1.display_info()
print()
bus1.display_info()
