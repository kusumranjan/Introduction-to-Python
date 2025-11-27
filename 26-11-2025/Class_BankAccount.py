    def __init__(self,Owner, balance = 0):
        self.Owner = Owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited:",amount)
        print("Current balance:",self.balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:",amount)
            print("Current balance:",self.balance)

        else:
            print("insufficient balance")

account1 = BankAccount("Kusum",500000)

account1.deposit(40000)
account1.withdraw(35000)
account1.withdraw(25000)
