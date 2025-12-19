input_string = "Pythonforbeginners is a great source to get started with Python."
mySet = set(input_string)
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
            countOfChar += 1
    print(element, countOfChar)
