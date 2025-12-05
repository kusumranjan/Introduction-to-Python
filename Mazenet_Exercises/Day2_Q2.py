

#Exercise 1 — Second Largest Number (Without Sorting)


nums = [23, 89, 12, 78, 55, 42]
largest = second_largest = float('-inf')
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)
#Exercise 2 — Move All Zeros to the End**


nums = [0, 3, 0, 5, 7, 0, 9]
non_zero_elements = [num for num in nums if num != 0]
zero_count = nums.count(0)
result = non_zero_elements + [0] * zero_count
print(result)
#Exercise 3 — Interchange First and Last Elements

lst = ['a', 'b', 'c', 'd', 'e']
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
#Exercise 4 — Extract Only Prime Numbers

nums = [10, 11, 12, 13, 17, 20, 23]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_nums = [num for num in nums if is_prime(num)]
print(prime_nums)
# Exercise 5 — Find All Indices of a Given Value**


nums = [5, 2, 7, 5, 9, 5, 3]
def find_indices(lst, value):
    return [i for i, num in enumerate(lst) if num == value]
value = 5
indices = find_indices(nums, value)
print(indices)
#Exercise 6 — Create a New List of Squares (Without Comprehension)


nums = [2, 4, 6, 8]
squares = []
for num in nums:
    squares.append(num ** 2)
print(squares)
```

---
