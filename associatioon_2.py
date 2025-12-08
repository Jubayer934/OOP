class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} is driving {car.model} which has {car.wheels} wheels. Car owner is {car.owner}.")
class Car:
    def __init__(self, model, wheels):
        self.model = model
        self.wheels = wheels
        self.owner = "Jubayer"
driver = Driver("Rahim")
car = Car("Toyota", 4)

driver.drive(car)   # Association
print(f"Car owner is still accessible: {car.owner}")