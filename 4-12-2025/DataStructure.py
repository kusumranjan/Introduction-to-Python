#6. Given a list of product prices, remove duplicates while maintaining order.

'''
li=[12,12,10,98,76,76]
lii=[]
for i in li:
    if i in lii:
        continue
    else:
        lii.append(i)
print(lii)

'''
#7. Merge two lists into a dictionary of {key: value} where list1 is keys and list2 is values.

'''
li=["Name","Roll","Age"]
lii=["Bishal",1,24]

d={}
j=0
for i in li:
    d[i]=lii[j]
    j+=1

print(d)
'''
#8. Given a dictionary of student marks, return the top 3 students.

'''

s = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "David": 95,
       "Eva": 88,
    "Frank": 90,
    "Grace": 80
}
top=dict(sorted(s.items(),key=lambda x:x[1],reverse=True)[:3])
print(top)
'''
#9. Flatten a nested list like [[1,2],[3,4],[5,6]] into a single list.

'''
li=[[1,2],[3,4],[5,6],7,8]
lii=[]
for i in li:
    if type(i)==list:
        for j in i:
            lii.append(j)
    else:
        lii.append(i)

print(lii)
'''

#10. Find common elements between three sets.
'''
s1={1,2,3}
s2={3,4,5,6}
s3={3,7,8,9}
li=[s1,s2,s3]
lii=[]
for i in li:
    if type(i) == set:
        for j in i:
            lii.append(j)
for i in set(lii):
    if lii.count(i)==3:
        print(i)
'''
#11. Convert a list of tuples to a dictionary only if keys are unique.


'''
data = [
    ("id", 101),
    ("name", "Alice"),
    ("age", 23),
     ("city", "Kolkata")
]
keys = [k for k, v in data]#here k for is used to conatin k eys in list
if len(set(keys))== len(keys):
    d = dict(data)
    print(d)
else:
    print("Not possible")
'''


#12. Given a tuple of names, return one tuple with unique names.


'''
names = ('Bishal', 'aunao', 'anainja', 'Bishal')
unique_list = []

for name in names:
    if names.count(name) == 1:  # only keep names that appear once
        unique_list.append(name)

unique_names = tuple(unique_list)
print(unique_names)
'''


#13. Build a program to reverse every alternate element in a list.

'''

def reverse(n):
    rev=0
    while n > 0:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev

li=[1,23,45,67,89]
for i in range(len(li)):
    if i%2!=0:
        s=reverse(li[i])
        li[i]=s

print(li)
'''

#14. From a dictionary of employees, filter only employees with salary above 60000.

'''
d={
    "Alice":2000,
    "Bob":3000,
    "Charlie":4000,
    "David":5000,
    "Eva":7000,
}

for i in d.keys():
    if d[i]>6000:
        print(d[i],i)
'''

#15. Given two dictionaries, combine them but sum values for matching keys.

'''
d1={"a":10,"b":20,"c":30}
d2={"a":12,"d":13,"e":14}
combine={}
for k,v in d1.items():
    if k in d2:
        combine[k]=v+d2[k]
    else:
        combine[k]=v


for k,v in d2.items():
    if k in combine:
        continue
    else:
        combine[k]=v
print(combine)

'''
