#24. Read a text file and count: characters, words, lines.

'''

with open("notex.txt","r") as f:
    con=f.read()

lines=con.split("\n")
print("No of lines",len(lines))

li=con.split()
print("No of words",len(li))

c = 0
for i in con:
    if i == ' ' or i == '\n':
        continue
    else:
        c += 1

print(c)

'''


#25. Create a CSV file storing 20 employees and read it back into a dictionary list.

'''
def creator():
    di={}
    with open("order.csv","w") as f:
        for i in range(20):
            s=input("Enter Employee Name: ")
            f.write(s+"\n")

    with open("order.csv","r") as f:
        conn=f.read()
        j=0
        for i in conn.split("\n"):
            di[j]=i
            j+=1

    print(di)
creator()
'''

#26. Write a program that appends log entries to a logfile with timestamps.
'''
from datetime import datetime
ct=datetime.now()
with open("notes.txt","a") as f:
    f.write(f"Log file with {ct}")
'''



#27. Build a program that loads a JSON file of products, adds a discount, and writes back.
'''
import json
with open("products.json","r")as f:
    data=json.load(f)
for i in data:
    i['price']=i['price']-(i['price']*0.1)
with open("products.json","w") as f:
    json.dump(data,f)
'''


#28. Split a text file into two files: first half and second half.''

'''

with open("notes.txt","r") as f:
    lines=f.readlines()
mid=len(lines) // 2
with open("notex.txt","w")as f:
    f.writelines(lines[:mid])
with open("two.txt","w")as f:
    f.writelines(lines[mid:])
'''



#29. Convert a CSV file to JSON using Python.
'''

import csv, json
with open("order.csv","r") as f:
    d=f.readlines()

with open("Product.json","w") as f:
    json.dump(d,f)
'''
