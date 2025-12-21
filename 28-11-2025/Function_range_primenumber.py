def find_prime(a, b):
    li = []
    for i in range(a, b + 1):
        t = True
        if i < 2:
            continue
        for j in range(2, i):  
            if i % j == 0:
                t = False
                break
        if t:
            li.append(i)
    return li

print(find_prime(2, 15))
