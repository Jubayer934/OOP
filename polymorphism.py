class Car:
    def move(self):
        print("Driving")

class Bishop:
    def move(self):
        print("Moving diagonally")

class Duck:
    def move(self):
        print("Swimming or flying")

# All objects can move, even though they're very different
things = [Car(), Bishop(), Duck()]

for _ in things:
    _.move()
