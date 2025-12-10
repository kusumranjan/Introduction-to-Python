Sure! Below are the solutions for the exercises you provided:

---

### 1. **Python Basics (4 Exercises)**

**1. Write a program to take three numbers as input and print the largest.**

```python
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest number
largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")
```

**2. Write a program to check if a given string is a palindrome.**

```python
# Taking input string
string = input("Enter a string: ")

# Checking if the string is a palindrome
if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
```

**3. Write a program to count how many times each character appears in a string.**

```python
from collections import Counter

# Taking input string
string = input("Enter a string: ")

# Counting character frequency
char_count = Counter(string)

# Printing the result
for char, count in char_count.items():
    print(f"'{char}' appears {count} times")
```

**4. Write a program to remove all special characters from a string.**

```python
import re

# Taking input string
string = input("Enter a string: ")

# Removing special characters using regex
cleaned_string = re.sub(r'[^A-Za-z0-9\s]', '', string)

# Printing the cleaned string
print(f"String without special characters: {cleaned_string}")
```

---

### 2. **Data Structures – Lists, Tuples, Sets, Dictionaries (8 Exercises)**

#### **Lists**

**1. Given a list of numbers, remove all duplicates without using set.**

```python
# Given list of numbers
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Removing duplicates
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Printing the result
print(f"List without duplicates: {unique_numbers}")
```

**2. Rotate a list to the right by N positions.**

```python
# Given list and N
numbers = [1, 2, 3, 4, 5]
N = 2

# Rotating the list
rotated_list = numbers[-N:] + numbers[:-N]

# Printing the result
print(f"List after rotating by {N} positions: {rotated_list}")
```

**3. Given a list of strings, return a new list containing only strings longer than 4 characters.**

```python
# Given list of strings
words = ["apple", "cat", "banana", "dog", "elephant"]

# Filtering strings longer than 4 characters
long_words = [word for word in words if len(word) > 4]

# Printing the result
print(f"Words longer than 4 characters: {long_words}")
```

#### **Tuples**

**1. Write a program to convert a list of tuples into a dictionary.**

```python
# Given list of tuples
tuples_list = [("a", 1), ("b", 2), ("c", 3)]

# Converting to dictionary
dictionary = dict(tuples_list)

# Printing the result
print(f"Converted dictionary: {dictionary}")
```

**2. Given a tuple of numbers, find the second largest number.**

```python
# Given tuple
numbers = (10, 20, 4, 45, 99)

# Finding the second largest number
unique_numbers = sorted(set(numbers), reverse=True)
second_largest = unique_numbers[1] if len(unique_numbers) > 1 else None

# Printing the result
print(f"The second largest number is: {second_largest}")
```

#### **Sets**

**1. Given two sets, find elements that are in either set but not in both (without symmetric difference operator).**

```python
# Given sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Elements that are in either set but not both
result = (set1 - set2) | (set2 - set1)

# Printing the result
print(f"Elements in either set but not both: {result}")
```

**2. Given a list, print only those elements whose frequency is exactly 2 using sets.**

```python
from collections import Counter

# Given list
numbers = [1, 2, 2, 3, 4, 4, 5]

# Counting frequency of elements
count = Counter(numbers)

# Printing elements with frequency exactly 2
result = {key for key, value in count.items() if value == 2}
print(f"Elements with frequency exactly 2: {result}")
```

#### **Dictionaries**

**1. Combine two dictionaries. If a key exists in both, create a list of values.**

```python
# Given dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Combining dictionaries
combined_dict = {}
for d in (dict1, dict2):
    for key, value in d.items():
        if key in combined_dict:
            combined_dict[key] = [combined_dict[key], value] if isinstance(combined_dict[key], list) else [combined_dict[key], value]
        else:
            combined_dict[key] = value

# Printing the result
print(f"Combined dictionary: {combined_dict}")
```

---

### 3. **Functions (5 Exercises)**

**1. Write a function that accepts a list of numbers and returns the average.**

```python
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Testing the function
numbers = [1, 2, 3, 4, 5]
print(f"Average: {average(numbers)}")
```

**2. Write a function that returns the factorial of a number.**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Testing the function
num = 5
print(f"Factorial of {num}: {factorial(num)}")
```

**3. Write a function that removes all vowels from a string.**

```python
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

# Testing the function
input_string = "Hello World"
print(f"String without vowels: {remove_vowels(input_string)}")
```

**4. Write a function that takes a start and end value and returns a list of prime numbers between them.**

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

# Testing the function
start = 10
end = 50
print(f"Prime numbers between {start} and {end}: {prime_numbers(start, end)}")
```

**5. Write a function that finds the longest word in a given sentence.**

```python
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Testing the function
sentence = "The quick brown fox jumped over the lazy dog"
print(f"The longest word is: {longest_word(sentence)}")
```

---

### 4. **Lambda Functions (3 Exercises)**

**1. Use lambda to sort a list of dictionaries by the key "age".**

```python
# List of dictionaries
people = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]

# Sorting by age using lambda
sorted_people = sorted(people, key=lambda x: x['age'])

# Printing the result
print(f"Sorted by age: {sorted_people}")
```

**2. Use lambda to compute squares of all elements in a list.**

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Computing squares using lambda
squares = list(map(lambda x: x**2, numbers))

# Printing the result
print(f"Squares of numbers: {squares}")
```

**3. Use lambda with filter to return only even numbers from a list.**

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering even numbers using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Printing the result
print(f"Even numbers: {even_numbers}")
```

---

These are the solutions for all the exercises you listed! If you need further clarifications or adjustments, feel free to ask.
