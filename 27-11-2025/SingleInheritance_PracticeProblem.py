#Vechile and Car

class Vechile:
    def __init__(self, brand):
        self.brand = brand

class Car(Vechile):
    def __init__(self, brand,Model):
        super().__init__(brand)
        self.Model = Model
c = Car("Toyota","Ford")
print(c.brand)
print(c.Model)

#Product and electronic product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectricProduct(Product):
    def __init__(self, name, price, warrenty):
        super().__init__(name, price)
        self.warrenty = warrenty
ep = ElectricProduct("Laptop",55000,"2 years")
print(ep.name, ep.price, ep.warrenty)
