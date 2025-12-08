class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10
    
    def brake(self):
        self.speed -= 10


# creating objects
car1 = Car("Toyota", "Red")
car2 = Car("Tesla", "White")

car1.accelerate()
car2.accelerate()
car2.accelerate()

print(f"The {car1.brand} which color is {car1.color}, the speed is = {car1.speed}")

print(f"The {car2.brand} which color is {car2.color}, the speed is = {car2.speed}")
