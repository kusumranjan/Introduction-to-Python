#Exercise 12: Square & Cube of a Number

number = int(input("Enter number: "))


square = number ** 2
cube = number ** 3


print(f"Square: {square}")
print(f"Cube: {cube}")

 # Exercise 13:Convert Minutes to Hours & Minutes


total_minutes = int(input("Enter minutes: "))


hours = total_minutes // 60
minutes = total_minutes % 60


print(f"{hours} hours and {minutes} minutes")

# Exercise 14 :Swap Two Variables

a = int(input("Enter a: "))
b = int(input("Enter b: "))


a, b = b, a


print(f"After swap → a = {a}, b = {b}")

# Exercise 15: Check Positive, Negative, or Zero

number = float(input("Enter a number: "))


if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Exercise 16: Find the Last Digit of a Number

number = int(input("Enter a number: "))


last_digit = number % 10


print(f"Last digit: {last_digit}")

#Exercise 17: Sum of First N Natural Numbers

N = int(input("Enter N: "))

total_sum = 0
for i in range(1, N+1):
    total_sum += i


print(f"Sum of first {N} natural numbers: {total_sum}")

# Exercise 18: Multiplication Table

number = int(input("Enter a number: "))


for i in range(1, 11):
   print(f"{number} x {i} = {number * i}")

#Exercise 19: Count Digits in a Number

number = int(input("Enter a number: "))


digit_count = 0
while number != 0:
    number //= 10  # Remove the last digit
    digit_count += 1


print(f"Total digits: {digit_count}")

# Exercise 20: Reverse a Number (Using Loops)



reversed_number = 0
while number != 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit
    number //= 10  

print(f"Reversed number: {reversed_number}")
