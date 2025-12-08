class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching.")

class Student:
    def __init__(self, name):
        self.name = name

    def learn(self):
        print(f"{self.name} is learning.")

teacher = Teacher("Mr. Ali")
student = Student("Jubayer")

# Association: student uses teacher, teacher uses student
teacher.teach()
student.learn()


