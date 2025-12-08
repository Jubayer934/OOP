class A:
    def showA(self):
        print("From A")

class B:
    def showB(self):
        print("From B")

class C(A, B):
    pass

c = C()
c.showA()  # From A
c.showB()  # From B