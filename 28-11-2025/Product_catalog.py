items=[]
with open("notex.txt", "r") as f:
    c=f.readlines()
    for x in c:
        p=x.strip().split(",")
        if len(p) == 2:
            name=p[0]
            price=(p[1])
            items.append([name,price])

with open("catalogs.txt","a") as f:
    for x in items:
        name=x[0]
        price=x[1]
        f.write(name+"      "+" ------"+"     "+str(price)+"\n")
