#exercise 1
try:
    a = float(input("enter a number one:"))
    b = float(input("enter a number two:"))
    result = a/b
    print(result)
except ZeroDivisionError:
    print(" can't divide by zero")
except ValueError:
    print(" please enter valid number")

#exercise 2
try:
    file = open("data.txt","r")

    content = file.read()
    print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print(f"Error: Permission denied to access '{file_path}'.")

#exercise 3
def string_to_int(value):
    try:
        number = int(value)
        return number
    except ValueError:
        return " invalid input"

#exercise 4

def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

my_list = [10, 20, 30]
print(safe_get(my_list, 1))   # Output: 20
print(safe_get(my_list, 5))   # Output: Index out of range


#exercise 6

class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError
    else:
        return "age is valid"

#exercise 7

def convert_list_items(lst):
    result = []

    for item in lst:
        try:
            number = int(item)
            result.append(number)
        except ValueError:
            print(f"Cannot convert '{item}' to number")
            result.append(none)
    return result

list = ["10", "20", "30", "abc"]

converted = convert_list_items(list)
print(converted)

#exercise 8

class LowBalanceError(Exception):
    """Custom exception to be raised when balance is insufficient."""
    def __init__(self, message="Insufficient balance for this withdrawal"):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    def __init__(self, balance=0):
        """Initializes a new bank account with an optional balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Withdraw money from the account if there are sufficient funds."""
        if amount > self.balance:
            
            raise LowBalanceError(f"Attempted withdrawal of {amount}, but balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")
            return self.balance



account = BankAccount(1000)  


try:
    print(f"Current Balance: {account.balance}")
    account.withdraw(1500)  
except LowBalanceError as e:
    print(f"Error: {e}")


try:
    print(f"New Balance after withdrawal: {account.withdraw(500)}")  
except LowBalanceError as e:
    print(f"Error: {e}")
  
#exercise 9
class LowBalanceError(Exception):
    """Custom exception to be raised when balance is insufficient."""
    def __init__(self, message="Insufficient balance for this withdrawal"):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    def __init__(self, balance=0):
        """Initializes a new bank account with an optional balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Withdraw money from the account if there are sufficient funds."""
        if amount > self.balance:
            # Raise LowBalanceError if balance is insufficient
            raise LowBalanceError(f"Attempted withdrawal of {amount}, but balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")
            return self.balance
account = BankAccount(1000)  # Account initialized with 1000 balance


try:
    print(f"Current Balance: {account.balance}")
    account.withdraw(1500)  
except LowBalanceError as e:
    print(f"Error: {e}")


try:
    print(f"New Balance after withdrawal: {account.withdraw(500)}")  
except LowBalanceError as e:
    print(f"Error: {e}")
#exercise 10


def write_to_file():
    file_name = "user_input.txt"
    try:
        
        user_text = input("Enter some text to save in the file: ")

        
        file = open(file_name, "w")
    except IOError:
        print("Error: Unable to open the file for writing.")
    else:
        try:
            
            file.write(user_text)
            print(f"Successfully written to {file_name}")
        except Exception as e:
            print(f"Error while writing to file: {e}")
        finally:
            
            file.close()
            print("File closed safely.")
    finally:
        print("Operation completed.")


write_to_file()
