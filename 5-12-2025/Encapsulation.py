class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance #private atttribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Account")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")


    def get_balance(self):
        return self.__balance

acc=BankAccount("Bishal",5000)
acc.deposit(100)
print(acc.get_balance())
acc.withdraw(200)
print(acc.get_balance())

acc.__balance=100000 #this will not modify as private attribute
print(acc.get_balance())
print(dir(acc))
