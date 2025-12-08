class Engine:
    def __init__(self, type):
        self.engine_type = type

    def start(self):
        print("➡️ Engine started")

    def stop(self):
        print("➡️ Engine stopped")

class wheels:
    def __init__(self, size):
        self.wheel_size = size

    def rotate(self):
        print("➡️ Wheels are rotating")

class battery:
    def __init__(self, capacity):
        self.battery_capacity = capacity

    def supply_power(self):
        print("➡️ Battery is supplying power")

class Car:
    def __init__(self, e, w, b):
        self.car_engine = Engine(e)   # Composition
        self.car_wheels = wheels(w)     # Composition  
        self.car_battery = battery(b)   # Composition
    
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def start_car(self):
        self.start()
        self.car_battery.supply_power()
        self.car_engine.start()
        self.car_wheels.rotate()
        print("Car is now running\n")

    def stop_car(self):
        self.stop()
        self.car_engine.stop()
        print("Car is now off\n")


my_engine = Engine("V8")
print(f"Engine type: {my_engine.engine_type}\n")

my_wheels = wheels(18)
print(f"Wheels size: {my_wheels.wheel_size} inches\n")

my_battery = battery(5000)
print(f"Battery capacity: {my_battery.battery_capacity} mAh\n")

# Now Composition the Car class uses the Engine class.

my_car = Car(e = "V8", w = 22, b = 10000)
my_car.start_car()
my_car.stop_car()

