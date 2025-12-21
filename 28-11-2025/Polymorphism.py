class Animal:
    def sound(self):
        print("I'm a animal")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d=Dog()
d.sound()
c=Cat()
c.sound()

#######################################################

class Notification:
    def send(self):
        print("Beep Sound")

class EmailNotification(Notification):
    def send(self):
        print("Email Arrived ring")

class SMSNotification(Notification):
    def send(self):
        print("Sms Arrived ring")

e=EmailNotification()
e.send()
s=SMSNotification()
s.send()
