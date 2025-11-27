#Exercise 6
class Product:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_cost(self):
        return self.price*self.quantity
p1 = Product("Milk",100,5)

print("Product name:", p1.name)
print("Total Cost:", p1.total_cost())

#Exercise 7

class Customer:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def check_loyalty(self):
        if self.age >= 25:
            return f"{self.name} is eligible for loyalty"
        else:
            return f"{self.name} is not  eligible for loyalty"
c1 = Customer("Rahul",28,"Kolkata")
c2 = Customer("Anita", 22 , "Delhi")

print(c1.check_loyalty())
print(c2.check_loyalty())

#Exercise 8

class BankAccount:
    def __init__(self,name ):
        self.name = name
        self.balance = 0
        self.logs = []

    def deposit(self,amount):
        self.balance += amount
        self.logs.append(f"deposited Rs{amount}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.logs.append(f"withdrew Rs{amount}")
        else:
            print("not enough money")
    def check_balance(self):
        print(f"Balance: {self.balance}")
    def show_logs(self):
        print("Transactions:")
        for log in self.logs:
            print("-",log)

acc = BankAccount("Rahul")
acc.deposit(10000)
acc.withdraw(100)
acc.check_balance()
acc.show_logs()

#Exercise 9

class Mobile:
    def __init__(self,brand,model,storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    def upgrade_storage(self,extra_storage):
        self.storage += extra_storage
        print(f"Storage upgraded! New storage: {self.storage} GB")

m1 = Mobile("Samsung", "Galaxy S21", 128)
print(f"Before upgrade: {m1.storage} GB")
m1.upgrade_storage(64)
print(f"After upgrade: {m1.storage} GB")

#Exercise 10

class Student:
    def __init__(self,name,s1,s2,s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def total_marks(self):
        return self.s1 + self.s2 + self.s3
    def percentage(self):
        return self.total_marks()/3
    def grade(self):

        percent = self.percentage()
        if percent >= 90:
            return "A"
        elif percent >= 75:
            return "B"
        elif percent >= 50:
            return "C"
        else:
            return "D"


s1 = Student("Rahul", 85, 90, 80)
print(f"Total Marks: {s1.total_marks()}")

print(f"Percentage: {s1.percentage():.2f}%")
print(f"Grade: {s1.grade()}")
