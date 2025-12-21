def write_content(emp_id,name,salary):
    record=f"""
    Employee Record
    Employee ID: {emp_id}
    Name: {name}
    Salary: {salary}
"""

    with open("employee.txt","w") as f:
        f.write(record)

write_content(101,"Bishal","4000")#here this will be over written as f.write removes previous content then writes
write_content(102,"Aman","5000")
