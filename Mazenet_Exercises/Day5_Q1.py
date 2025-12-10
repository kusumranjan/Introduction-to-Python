5.File Handling (5 Exercises)

1. Write a program to create a file and write 5 lines into it.


# Creating a file and writing 5 lines into it
with open("file.txt", "w") as file:
    file.write("Line 1: Python is great.\n")
    file.write("Line 2: File handling is important.\n")
    file.write("Line 3: Writing to files is easy.\n")
    file.write("Line 4: Python makes it simpler.\n")
    file.write("Line 5: Let's keep learning.\n")
2. Write a program to read a file and count the number of lines containing the word "Python".**

```python
# Reading the file and counting lines with "Python"
count = 0
with open("file.txt", "r") as file:
    for line in file:
        if "Python" in line:
            count += 1
print(f"Number of lines containing 'Python': {count}")
```

**3. Write a program to append a timestamped log entry into a file.**

```python
import datetime

# Append a timestamped log entry
with open("logfile.txt", "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"Log entry at {timestamp}: Log message.\n")
```

**4. Read a CSV file and print only rows where marks > 75.**

```python
import csv

# Reading the CSV file and filtering rows
with open("marks.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if int(row[1]) > 75:  # Assuming marks are in the second column
            print(row)
```

**5. Create a file that stores the squares of numbers from 1 to 20.**

```python
# Writing squares of numbers from 1 to 20 into a file
with open("squares.txt", "w") as file:
    for i in range(1, 21):
        file.write(f"{i}^2 = {i**2}\n")
```

---

### 6. **Classes & Objects (5 Exercises)**

**1. Create a class Book with title, author, pages. Add method to check if pages > 300.**

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

book = Book("War and Peace", "Leo Tolstoy", 400)
print(f"Is the book long? {book.is_long()}")
```

**2. Create a class BankAccount with deposit and withdraw methods.**

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
```

**3. Create a class Rectangle with methods to calculate area and perimeter.**

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
```

**4. Create a class Student that stores marks of three subjects and calculates percentage.**

```python
class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def percentage(self):
        total = self.marks1 + self.marks2 + self.marks3
        return (total / 300) * 100

student = Student(85, 90, 88)
print(f"Percentage: {student.percentage()}%")
```

**5. Create a class Mobile with brand, model, and method to show details.**

```python
class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

mobile = Mobile("Apple", "iPhone 13")
mobile.show_details()
```

---

### 7. **Constructors & Methods (3 Exercises)**

**1. Create a class Employee with constructor and method to print details.**

```python
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")

employee = Employee("Alice", 30, "Software Developer")
employee.print_details()
```

**2. Create a class Temperature with constructor and methods to convert Celsius to Fahrenheit and vice versa.**

```python
class Temperature:
    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    def celsius_to_fahrenheit(self):
        if self.unit == 'C':
            return (self.temperature * 9/5) + 32
        return self.temperature

    def fahrenheit_to_celsius(self):
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9
        return self.temperature

temp = Temperature(100, 'C')
print(f"100°C in Fahrenheit: {temp.celsius_to_fahrenheit()}°F")
```

**3. Create a class Laptop with constructor taking brand, RAM, price, and method to calculate discount.**

```python
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def calculate_discount(self, discount_percentage):
        return self.price - (self.price * discount_percentage / 100)

laptop = Laptop("Dell", "16GB", 800)
print(f"Price after 10% discount: {laptop.calculate_discount(10)}")
```

---

### 8. **Inheritance (4 Exercises)**

**1. Create parent class Vehicle and child class Car that overrides a method start().**

```python
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

car = Car()
car.start()
```

**2. Create Person → Employee → Manager (multilevel). Add different methods in each.**

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def work(self):
        print(f"Employee {self.name} is working.")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def manage(self):
        print(f"Manager {self.name} is managing {self.department}.")

manager = Manager("Alice", 101, "HR")
manager.greet()
manager.work()
manager.manage()
```

**3. Create a base class Payment and child classes: CreditCardPayment and UPIPayment. Override process().**

```python
class Payment:
    def process(self):
        pass

class CreditCardPayment(Payment):
    def process(self):
        print("Processing Credit Card Payment.")

class UPIPayment(Payment):
    def process(self):
        print("Processing UPI Payment.")

payment1 = CreditCardPayment()
payment1.process()

payment2 = UPIPayment()
payment2.process()
```

**4. Create two parent classes Camera and Phone, and a child class SmartPhone (multiple inheritance).**

```python
class Camera:
    def capture(self):
        print("Capturing photo")

class Phone:
    def call(self):
        print("Making a call")

class SmartPhone(Camera, Phone):
    def browse(self):
        print("Browsing the internet")

smartphone = SmartPhone()
smartphone.capture()
smartphone.call()
smartphone.browse()
```

---

### 9. **Polymorphism & Method Overriding (2 Exercises)**

**1. Create two classes Cat and Dog. Both should have a method sound() that behaves differently.**

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

cat = Cat()
dog = Dog()

cat.sound()
dog.sound()
```

**2. Create a Notification parent class and override send() in EmailNotification and SMSNotification.**

```python
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
```


```
    print("Sending Email")
```

class SMSNotification(Notification):
def send(self):
print("Sending SMS")

email = EmailNotification()
sms = SMSNotification()

email.send()
sms.send()

````

---

### 10. **Operator Overloading (1 Exercise)**

**1. Create a class Score that overloads the + operator to combine two scores, and overloads > to compare them.**

class Score:
    def __init__(self, score):
        self.score = score

    def __add__(self, other):
        return Score(self.score + other.score)

    def __gt__(self, other):
        return self.score > other.score

score1 = Score(90)
score2 = Score(85)
combined_score = score1 + score2
print(f"Combined Score: {combined_score.score}")
print(f"Is score1 greater than score2? {score1 > score2}")
````


