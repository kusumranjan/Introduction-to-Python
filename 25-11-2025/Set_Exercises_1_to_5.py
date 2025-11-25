#Exercise 1


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


result = (set1 | set2) - (set1 & set2)

print(result)

#Exercise 2


data = [1, 2, 2, 3, 4, 3, 5]


result = []
for item in data:
    if item not in result:
        result.append(item)

print(result)

#Exercise 3


numbers = {2, 4, 6, 8, 10}
target = 12


pairs = []
for x in numbers:
    y = target - x
    if y in numbers and x <= y:
        pairs.append((x, y))

print(pairs)

#Exercise 4



set1 = {1, 2, 3}
set2 = {4, 5, 6}


if set1 & set2 == set():
    print("Disjoint: True")
else:
    print("Disjoint: False")

#Exercise 5

words = ["apple", "banana", "grape"]


unique_chars = set()


for word in words:
    for char in word:
        unique_chars.add(char)

print(unique_chars)
