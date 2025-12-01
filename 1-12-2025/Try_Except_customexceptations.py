#custom expectation

class LowBalance(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds")
    return balance-amount
