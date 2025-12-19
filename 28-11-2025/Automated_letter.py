def automated_letter(name,course):
    report=f"""
    Hi {name} welcome to our course named {course}.
"""
    with open("notex.txt","a")as f:
        f.write(report)

s=input("enter your name")
y=input("enter your course")
automated_letter(s,y)
