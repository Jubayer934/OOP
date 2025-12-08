# OOP
OOP is a way of programming where we model real-world entities as objects that have data and methods. We use classes as blueprints to create these objects, and it helps make code more organized, reusable, and easier to manage using concepts like inheritance, polymorphism, encapsulation, and abstraction.

**(Example: class&object.py)**

## What is a Class
A class is a blueprint or template for creating objects.
It defines:

- What data (attributes/properties/fields) the objects will have.
- What behavior (methods/functions) the objects can perform.

## What is an Object

An object is an example of a class.

- Data (information about it)

- Behaviors (things it can do)

---
**Data** typically represents the individual information of an object.

**Methods** are the actions or behaviors of a class — the things its objects can do.

**Parameters** are the inputs you give to the method so it can do its job.

---

## ✅ Function vs Method (Easy Explanation)

### 1️⃣ Function

- A function is a block of code that performs a task.

- It is not attached to any object or class.

- You can call it directly.

### 2️⃣ Method

- A method is a function that belongs to a class.

- You must create an object to use it.

- It works on the object's data.

---
## 🧩 What is Composition? (Simple Explanation)

Composition means building a class using other classes.
Or in simple words: A big object is made from smaller objects.

### Example in real life:

A Car is made of:
Engine, 
Wheels, 
Steering, Battery

The car has an engine, has wheels, etc.
This “has-a” relationship is composition.

**(Example: compositon.py)**

## ⭐ What is Association? (Simple Definition)

 A relationship where one object uses another object. They can work together but can also exist independently.

### Real-life examples
✔ Teacher — Student

A teacher teaches students.
A student learns from teachers.

But:
- A teacher can exist without students

- A student can exist without teachers

This is association.

**(Example: association.py)**

## ⭐ What is Aggregation? (Simple Definition)

**Aggregation** is a special type of Association where one object contains another object,
BUT the contained object can exist independently.

### Real-Life Example of Aggregation

- A university has students

- But if the university closes, the student still exists

- The student also exists before joining the university

➡️ That is Aggregation.

**(Example: aggretion.py)**

## ⭐ What is Inheritance?

**Inheritance** allows one class to take (inherit) the properties and methods of another class.

- The new class is called the child/subclass
- The original class is called the parent/superclass

### Real-Life Example
A Car is a type of Vehicle. So everything a Vehicle can do, a Car can also do (plus more).

**(Example: Inheritance.py)**

---
**Override** (Method Overriding) is a core OOP concept where a child class replaces a method that already exists in the parent class.

Simple meaning:
- The parent has a method
- The child writes a new version of the same method
- The child version overrides (replaces) the parent version

**Method Overloading** is when multiple methods have the same name but different parameters (different number or types of arguments) in the same class.

It allows the same method name to do different things depending on how it’s called.

**Multiple Inheritance** happens when a child class inherits from more than one parent class.



**(Example: Method_Override.py & Method_Overload.py & Multiple_Inheritance.py)**

---

## ⭐ Polymorphism

Polymorphism means one interface, multiple forms.

You can call the same method on different objects, and each object will respond in its own way

**(Example: polymorphism.py)**

## ⭐ Abstraction
**Abstraction** means hiding the complex details of how something works and showing only the important features. You don’t care how it works internally; you just care about what it does. It helps simplify complex systems and makes your code easier to use and maintain.

### Real-world example

Think about driving a car:

You don’t need to know how the engine works or how the transmission moves the wheels.

You only need to know the interface:

- Press the accelerator → car moves

- Press the brake → car stops

- Turn the steering wheel → car turns

The internal workings are hidden from you. This is abstraction.

## ⭐ Encapsulation 

**Encapsulation** means hiding the internal data of an object and restricting direct access to it, while providing methods to safely read or modify that data.

It protects the object’s data from accidental changes.

It allows you to control how the data is accessed or updated.

Real-world example

Think of a bank account:

- The account balance is private.

- You cannot just change it directly.

- You can only deposit or withdraw money through methods (functions) that control the rules.

**(Example: encaptulation.py)**

## The difference between Abstraction and Encapsulation

|                       | Abstraction                                | Encapsulation                                   |
|-----------------------|--------------------------------------------|-------------------------------------------------|
| **Focus**             | What an object does                        | How data is hidden and protected                |
| **Purpose**           | Hide complexity, show only essential info  | Protect data, control access                    |
| **How implemented**   | Abstract classes, interfaces, methods      | Private/protected fields + public getters/setters |
| **Example**           | `Vehicle.start()` <br> `Animal.makeSound()`| `private double balance;` <br> `getBalance()`   |


---
---
# ⭐ 4 main OOP concepts with simple explanations
**Encapsulation** – Hiding data, controlling access

- Idea: Keep data private and allow controlled access via methods.

- Purpose: Protect data from accidental changes.
- Key: You cannot directly access __balance, only through methods.

**Abstraction** – Hiding complexity, showing only essentials

- Idea: Focus on what an object does, not how it does it.

- Purpose: Simplify complex systems.

- Key: You only interact with start(), the details are hidden.

**Inheritance** – Reusing code from a parent class

- Idea: A class can inherit properties and methods from another class.

- Purpose: Avoid code duplication and establish a relationship.

- Key: You call speak() on different objects, and each behaves differently.

**Polymorphism** – Same method, different behavior

- Idea: One method name can work with different types of objects.

- Purpose: Flexible and extensible code.

- Key: You call speak() on different objects, and each behaves differently.