#Example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s3 = Student("Abdullah",18)
s4 = Student("Rahul",28)

print(s3.name,s4.age)

#Exercise 

class Car:
    def __init__(self,brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)

# Creating three car objects
car1 = Car("Mercedes","Fortuner",450000)
car2 = Car("Hyundai","Creta",18000000)

car1.display()
print()
car2.display()
print()

#Example

class Employee:
    def __init__(self,emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("Employee ID:",self.emp_id)
        print("Name:",self.name)
        print("Department:",self.department)
        print("Salary:",self.salary)

# Creating employee objects

e1 = Employee(101,"Kusum","IT",36000)
e2 = Employee(102,"Rahul","IT",500000)

#Display details
e1.display()
print()

e2.display()
print()

#example

class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1+self.m2+self.m3

    def percentage(self):
        return(self.total()/300)*100
    def display(self):
        print("name:",self.name)
        print("Marks:",self.m1,self.m2,self.m3)
        print("Total:",self.total())
        print("Percentage:",self.percentage())

s1 = Student("Kusum",85,90,95)

s1.display()
