class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def check(self):
        if self.pages >300:
            print("True")
        else:
            print("False")


b=Book("W", "W", 300)
b.check()
############################################

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


    def print_balance(self):
        print(self.name)
        print(self.balance)

bank=Bank("Bishal", 100)
bank.deposit(100)
bank.withdraw(10)
bank.print_balance()
##########################################


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.width = b

    def area(self):
        print("Area of Rectangle", (self.length * self.width))

    def perimeter(self):
        print("Perimeter of Rectangle", (2*(self.length + self.width)))

r=Rectangle(10,20)
r.area()
r.perimeter()


###############################################

class Student:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def percent(self):
        c=(self.a+self.b+self.c)/3
        print(c)
        #as marks total is 300/100=3


s=Student(87,90,89)
s.percent()


####################################################

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display(self):
        print(self.brand, self.model)
        
m=Mobile("Vivo", "x3")
m.display()
