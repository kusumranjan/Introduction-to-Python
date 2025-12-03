import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='my0wn$ql0ff1ce',
    database='company_db'
)
cursor = conn.cursor()
#performing right join to print employees from a department
#cursor.execute('Select e.emp_name,e.emp_id,d.dept_name from employees e Right Join departments d on e.dept_id = d.dept_id')
#Reading data for employees with salary above 50000
#cursor.execute("SELECT * FROM  employees where salary>50000")
#Updating the dept_id for employee Imran ALi
"""emp_name = "Imran Ali"
cursor.execute("Update employees Set dept_id = 40 where emp_name = %s",(emp_name,))"""
#Deleting from departments table where location is Mumbai
"""loc = "Mumbai"
cursor.execute("Delete from departments where location = %s",(loc,))
rows = cursor.fetchall()"""
for row in rows:
    print(row)

cursor.close()
conn.close()
