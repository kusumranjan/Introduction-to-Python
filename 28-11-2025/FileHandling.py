with open("notes.txt", "r") as f:
    for line in f:
        if "Python" in line:  
            print(line, end="") 
######################################

with open("notes.txt","a")as f:
    for i in range(1,21):
        g=i**2
        f.write(str(g)+"\n")

#####################################

with open("notes.txt", "w") as f:
    f.write("Hello World\n")
    f.write("My name is Bishal\n")
    f.write("My name is Bishal\n")
    f.write("My name is Bishal\n")
    f.write("My name is Bishal\n")


with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

####################################

import csv

with open("oprder.csv","r")as f:
    reader = csv.reader(f)
    header=next(reader)
    for i in reader:
        m=int(i[1])
        if m>75:
            print(i)

#####################################

import time
with open("log.txt", "a") as log:
    log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
  
