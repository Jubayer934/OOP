class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

math_op = MathOperations()

print(math_op.add(5))        # 5 (only one argument)
print(math_op.add(5, 10))    # 15 (two arguments)
print(math_op.add(5, 10, 15))# 30 (three arguments)
