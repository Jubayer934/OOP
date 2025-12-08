class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.eat()   # inherited from Animal
d.bark()  # own method

c = Cat()
c.eat()   # inherited from Animal
c.meow()  # own method