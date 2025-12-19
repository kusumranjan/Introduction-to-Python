class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)

e=Employee("John", 5000)
e.display()

#########################################

class Temperature:
    def __init__(self,cel,fah):
        self.cel=cel
        self.fah=fah


    def cel_to_fahrenheit(self):
        return (self.cel * 1.8) + 32

    def fahrenheit_to_cel(self):
        return (self.fah -32 )/1.8

    def disply(self):
        print(self.cel_to_fahrenheit(),self.fahrenheit_to_cel())


t=Temperature(cel=23,fah=21)
t.disply()
#########################################

class Laptop:
    def __init__(self, name, brand,ram, price):
        self.name = name
        self.brand = brand
        self.price = price
        self.ram = ram

    def discount(self):
        p=self.price-(self.price*0.15)
        print(f"Your {self.name}'s price is {self.price}")



l=Laptop("del34","del",34000)
l.discount()

#####
