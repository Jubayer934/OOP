class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Student: {self.name}")

class University:
    def __init__(self, name):
        self.name = name
        self.students = []   # list of Student objects (Aggregation)

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"University: {self.name}")
        for _ in self.students:
            _.show()

# Students created independently
s1 = Student("Jubayer")
s2 = Student("Rahim")

# University aggregates them
uni = University("Manarat International University")
uni.add_student(s1)
uni.add_student(s2)

uni.show_students()

del uni

print("\nAfter deleting University:")
s1.show()  # Student still exists after University is deleted
s2.show()  # Student still exists after University is deleted