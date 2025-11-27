#Animal, Mammal and DOG

class Animal:
    def __init__(self, species):
        self.species = species
class Mammal(Animal):
    def __init__(self, species, has_hair):
        super().__init__(species)
        self.has_hair = has_hair
class Dog(Mammal):
    def __init__(self, species, has_hair, breed):
        super().__init__(species, has_hair)
        self.breed = breed
d = Dog("Canine",True, "Golden Retriever")
print(d.species, d.has_hair, d.breed)

#Device , computer and Laptop
class Device:
    def __init__(self,brand):
        self.brand = brand
class Computer(Device):
    def __init__(self, brand, processor):
        super().__init__(brand)
        self.processor = processor
class laptop(Computer):
    def __init__(self, brand, processor, battery_life):
        super().__init__(brand, processor)
        self.battery_life = battery_life
L = laptop("Dell","Intel i7",8)
print(L.brand, L.processor, L.battery_life)
