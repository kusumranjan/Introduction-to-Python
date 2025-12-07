#Exercise 6:Class `Product` with Attributes and Method to Calculate Total Cost


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


product = Product("Laptop", 1000, 5)
print(f"Total cost of {product.name}: {product.total_cost()}")

#Exercise 7: Class `Customer` with Eligibility for Loyalty Program**


class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def eligible_for_loyalty(self):
        return self.age > 25


customer = Customer("Alice", 30, "New York")
print(f"Is {customer.name} eligible for loyalty program? {customer.eligible_for_loyalty()}")


#Exercise 8:Class `BankAccount` with Deposit, Withdraw, and Balance Check


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_log = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_log.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_log.append(f"Withdrew: {amount}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.balance

    def display_transactions(self):
        for transaction in self.transaction_log:
            print(transaction)

account = BankAccount("John", 500)
account.deposit(200)
account.withdraw(100)
account.display_transactions()
print(f"Balance: {account.check_balance()}")

#Exercise 9:Class `Mobile` with Method to Upgrade Storage


class Mobile:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def upgrade_storage(self, new_storage):
        self.storage = new_storage


mobile = Mobile("Apple", "iPhone 12", 64)
print(f"Before upgrade: {mobile.storage}GB")
mobile.upgrade_storage(128)
print(f"After upgrade: {mobile.storage}GB")

#Exercise 10 : Class `Student` with Methods for Total, Percentage, and Grade

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total_marks(self):
        return self.marks1 + self.marks2 + self.marks3

    def percentage(self):
        return (self.total_marks() / 300) * 100

    def grade(self):
        perc = self.percentage()
        if perc >= 90:
            return "A"
        elif perc >= 75:
            return "B"
        elif perc >= 60:
            return "C"
        elif perc >= 45:
            return "D"
        else:
            return "F"

student = Student("Jake", 85, 78, 92)
print(f"Total Marks: {student.total_marks()}")
print(f"Percentage: {student.percentage()}%")
print(f"Grade: {student.grade()}")
