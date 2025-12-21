s=input("Enter a string")
iny=""
for i in s:
    if i == " " or i=="#" or i=="$" or i=="@" or i=="^":
        continue
    else:
        iny+=i

print(iny)
