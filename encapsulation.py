class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (note the double underscore)
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    # Method to check balance
    def get_balance(self):
        return self.__balance

# Using the class
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Trying to access balance directly
print(account.__balance)  # Error! Cannot access private variable
