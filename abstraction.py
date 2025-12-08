from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # We don't define how; subclasses will define

# Subclass implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Using abstraction
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())

# shape = Rectangle(4, 5)
# print("Area of Rectangle:", shape.area())

# shape = Circle(3)
# print("Area of Circle:", shape.area())
