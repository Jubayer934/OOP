class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show(self):
        print(f"Name: {self.name}. Lives in: {self.address}")

class Student(Person):
    def __init__(self, name, student_id, address):
        super().__init__(name, address)   # call parent constructor
        self.student_id = student_id

    def show_student(self):
        print(f"ID: {self.student_id}")

s = Student("Jubayer", 101, "Dhaka")
s.show()          # from Person
s.show_student()  # from Student
