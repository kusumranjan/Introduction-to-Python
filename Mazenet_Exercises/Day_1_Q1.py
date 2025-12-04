#Exercise 6: Create a class Product with attributes name, price, quantity. Add a method to calculate the total cost of all quantities. 

  class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_cost(self):
        return self.price * self.quantity


product = Product("Laptop", 1000, 5)
print(f"Total cost of all quantities: ${product.total_cost()}")

#Exercise 7 Create a class Customer with attributes name, age, city. Add a method that checks if the customer is eiigible for a loyalty program (age > 25).

class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def is_eligible_for_loyalty(self):
        return self.age > 25


customer = Customer("Alice", 30, "New York")
print(f"Is customer eligible for loyalty program? {customer.is_eligible_for_loyalty()}")

#Exercise 8: Create a class BankAccount that supports deposit, withdraw, check balance, and displays transaction logs. 

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        return self.balance
    
    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)


account = BankAccount("Bob")
account.deposit(500)
account.withdraw(200)
account.display_transactions()
print(f"Current balance: ${account.check_balance()}")

# Exercise 9 Create a class Mobile with attributes brand, model, storage. Add a method to upgrade storage. 

class Mobile:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def upgrade_storage(self, new_storage):
        self.storage = new_storage
        print(f"Storage upgraded to {new_storage}GB")


mobile = Mobile("Apple", "iPhone 13", 64)
print(f"Current storage: {mobile.storage}GB")
mobile.upgrade_storage(128)

# Exercise 10 Create a class Student with three subject marks. Add methods for total, percentage, and grade (A, B, C, D).

class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def total(self):
        return self.marks1 + self.marks2 + self.marks3
    
    def percentage(self):
        return (self.total() / 300) * 100
    
    def grade(self):
        percentage = self.percentage()
        if percentage >= 90:
            return 'A'
        elif percentage >= 75:
            return 'B'
        elif percentage >= 60:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'


student = Student(85, 90, 78)
print(f"Total marks: {student.total()}")
print(f"Percentage: {student.percentage()}%")
print(f"Grade: {student.grade()}")

