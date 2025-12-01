def calculate_total(a, b):
    total = a + b
    print("Debug: a = ", a)
    print("Debug: b = ", b)
    print("Debug: total = ", total)
    result = total/0
    print("the result is:", result)

calculate_total(1,2)

#correct code 


def calculate_total(a, b):
    total = a + b
    print("Debug: a =", a)
    print("Debug: b =", b)
    print("Debug: total =", total)

    try:
        result = total / 0  
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


calculate_total(1, 2)
