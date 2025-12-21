def total_summary(name,quantity,price):
    total = quantity * price
    with open("catalogs.txt","a") as f:
        f.write(name+"  "+str(quantity)+"  "+str(price)+"\n")
    return total


total=0
for i in range(3):
    s=str(input("Enter Name:"))
    iin=int(input("Enter Quantity:"))
    iiin=int(input("Enter Price:"))
    st=total_summary(s,iin,iiin)
    total+=st

with open("catalogs.txt","a") as f:
    f.write(str(total)+"\n")
