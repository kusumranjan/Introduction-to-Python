#16. Build a Student class storing id, name, and marks. Add methods to calculate grade.
'''
class Student:
    def __init__(self, name,id, marks1,marks2,marks3):
        self.name = name
        self.id = id
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def grade_Calculator(self):
        total_marks = (self.marks1 + self.marks2 + self.marks3) / 3
        return total_marks

s=Student("Monu", 1, 92,98,97)
st=s.grade_Calculator()
if st >=9:
    print("Grade A")

elif st>=8 & st<=9:
    print("Grade B")

elif st>=7 & st<=8:
    print("Grade C")

else:
    print("Grade D")

'''

#17. Implement a Product → ElectronicProduct (inheritance) where Electronics adds warranty years.

'''
class Product:
    def __init__(self,id):
        self.id = id

class ElectronicProduct(Product):
    def __init__(self,id,warranty,name):
        super().__init__(id)
        self.warranty = warranty
        self.name = name
    def display(self):

        print("Name",self.name)
        print("Id",self.id)
        print("Warranty",self.warranty)

e=ElectronicProduct(1,"2","Phone")
e.display()
'''
#18. Create a Payment class with credit-card and UPI subclasses overriding process_payment().

'''
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print("Processing payment...")

class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process_payment(self):
        print(f"Processing ₹{self.amount} through Credit Card: {self.card_number}")

class UPI(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process_payment(self):
        print(f"Processing ₹{self.amount} through UPI ID: {self.upi_id}")


# Example# Example usage
p1 = CreditCard(1500, "1234-5678-9876")
p2 = UPI(800, "bishal@upi")

p1.process_payment()
'''

#19. Create a Vehicle class and Car, Bike subclasses. Override max_speed().

'''
class Vehicle:
    def __init__(self, wheeler,name):
        self.wheeler = wheeler
        self.name=name
    def max_speed(self):
        print(f"{self.name} is a {self.wheeler}wheeler with max speed of")

class Bike(Vehicle):
    def __init__(self, wheeler, name ,speed):
        super().__init__(wheeler,name)
        self.speed = speed

    def max_speed(self):
        print(f"{self.name} is a {self.wheeler}wheeler with max speed of{self.speed}")


class Car(Vehicle):
    def __init__(self, wheeler, name, speed):
        super().__init__(wheeler, name)
        self.speed = speed

    def max_speed(self):
        print(f"{self.name} is a {self.wheeler}wheeler with max speed of{self.speed}")


b=Bike(2,"Honda",125)
c=Car(4,"Mercedes",300)
b.max_speed()
c.max_speed()
'''


#20. Implement Operator Overloading: add two objects of BankAccount to return total balance.


'''
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


# Example usage
acc1 = BankAccount(1000)
acc2 = BankAccount(2000)

print(acc1 + acc2)  
'''



#21. Build a ShoppingCart class implementing add, remove, total, apply_discount.

'''
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, item, price):
        self.items[item] = price
        print(f"Added {item} for ₹{price}")

    def remove(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Removed {item}")
        else:
            print(f"{item} not found in cart")

    def total(self):
        return sum(self.items.values())

    def apply_discount(self, percent):
        discount = (percent / 100) * self.total()
        return self.total() - discount


cart = ShoppingCart()
cart.add("Shoes", 1500)
cart.add("Bag", 1000)
cart.remove("Shoes")

print("Total:", cart.total())
print("Total after 10% discount:",cart.apply_discount(10))
'''




#22. Create a Library class to store books and a method to search by title or author.


'''
class Library:
    def __init__(self):
        self.books = {}  

    def add(self, title, author):
        self.books[title] = author
        print(f"'{title}' by {author} added to library")

    def show_books(self):
        print("Books in library:")
        for title, author in self.books.items():
            print(f"{title} by {author}")

    def search_book(self, keyword):
        found = False
        for title, author in self.books.items():
            if keyword.lower() in title.lower() or keyword.lower() in author.lower():
                print(f"Found: {title} by {author}")
                found = True
        if not found:
            print("No matching book found")


# Example usage
lib = Library()
lib.add("Dracula", "Bram Stoker")
lib.add("Frankenstein", "Mary Shelley")

lib.show_books()
lib.search_book("Bram")
lib.search_book("Dracula")
'''





#23. Create a User class and an Admin subclass that can delete a user (override methods).


'''
class User:
    def __init__(self, user_type):
        self.type = user_type
        self.li = []

    def power(self):
               print(f"{self.type} power")

    def display(self):
        print(self.li)


class Admin(User):
    def __init__(self):
        super().__init__("Admin")

    def add_user(self, name):
        self.li.append(name)
        print(f"Added {name}")

    def power(self, name):
        if name in self.li:
            self.li.remove(name)
            print(f"Deleted {name}")
        else:
            print(f"{name} not found")


a = Admin()
a.add_user('a')
a.add_user('b')
a.display()
a.power('b')
'''
