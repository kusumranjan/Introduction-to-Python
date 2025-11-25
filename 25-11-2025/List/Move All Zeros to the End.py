num = [0,3,5,7,0,9]
temp = []
zeros = []

for i in range(len(num)):
    if num[i] != 0:
        temp.append(num[i])
    else:
        zeros.append(num[i])
print(temp+zeros)
