#exercise 1
mixed = (1,"a",2,"b",3,"c")

num = []
strings = []

for item in mixed:
    if type(item) == str:
        strings.append(item)
    else:
        num.append(item)
nums = tuple(num)
strings = tuple(strings)
print(nums)
print(strings)

#exercise 2


numbers = (1, 2, 3, 4, 5)

is_increasing = True
for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        is_increasing = False
        break

print("Strictly Increasing:", is_increasing)

#exercise 3


words = ("python", "cloud", "data")

reversed_words = tuple(word[::-1] for word in words)

print(reversed_words)

#exercise 4


data = (1, 2, 3, 2, 4, 2)
value = 2


positions = [i for i in range(len(data)) if data[i] == value]

print("Index positions:", positions)

#exercise 5



data = (10, (20, 30), (40, (50, 60)))

def print_numbers(t):
    for item in t:
        if type(item) is int:
            print(item)
        else:
            print_numbers(item)

print_numbers(data)
