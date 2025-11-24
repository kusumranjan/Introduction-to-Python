name = "Kusum Ranjan"
age = 22
salary = 4.8

print(name)
print(age)
print(salary)
# arthematic
a = 10
b = 3
print("addition",a+b)
print("division ",a/b)
print("floor divison " , a%b)
print('power',a**b)

#list number till 20


for i in range(1, 21):
    if i % 2:  
        print(i, "is odd")
    else:      
        print(i, "is even")
 # elif       
marks = int(input("enter your score:"))

if marks >=90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
# for loop    
for i in range(1,6):
    print("Number:", i)
#while loop iterator    
    
counter = 1


while counter <= 5:
    print("count:", counter)
    counter += 1
#break

for i in range(10):
    if i == 5:
        break
    print(i)
 #continue   
for i in range(10):
    if i %2 == 0:
        continue
    print(i)

#list 

numbers = [10,20,30,40]
names = ["kusum","Ranjan","Neha"]
mixed = [10,"hello",3.5,True]
print(numbers)

fruits = ["apple", "banana","orange","cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

fruits.append("mango")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

fruits = ["apple", "banana", "orange"]

fruits.remove("banana")
fruits.pop(2)
fruits.pop()
del fruits[0]
