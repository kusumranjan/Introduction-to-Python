class Phone:
    def __init__(self, battery, brand):
        self.battery = battery
        self.brand = brand

    def display(self):
        print(self.battery)
        print(self.brand)

class Camera:
    def __init__(self,fmp,bmp):
        self.fmp = fmp
        self.bmp = bmp

    def display_(self):
        print(self.fmp,self.bmp)

class SmartPhone(Phone,Camera):
    def __init__(self,battery,brand,fmp,bmp):
        Phone.__init__(self,battery,brand)
        Camera.__init__(self,fmp,bmp)

    def d(self):
        self.display()
        self.display_()

s=SmartPhone(3200,"iphone",32,64)
s.d()
###################################################################

class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting the car engine...")

v = Vehicle()
v.start() 

c = Car()
c.start()  

#########################################################################3



class Payment:
    def process(self):
        print("Processing payment...")

class CreditCardPayment(Payment):
    def process(self):
        print("Processing credit card payment...")

class UPIPayment(Payment):
    def process(self):
        print("Processing UPI payment...")

p1 = CreditCardPayment()
p1.process()   

p2 = UPIPayment()
p2.process() 


######################################################################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_employee_info(self):
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_manager_info(self):
        print(f"Manager of Department: {self.department}")

# Test
m = Manager("Alice", 35, "E101", 85000, "IT")
m.show_person_info()     
m.show_employee_info()    
m.show_manager_info() 
