import time
def attendance_checker(name,status,timestamp):
    report=f"""
    Name={name}
    Status={status}
    Timestamp={timestamp}
"""
    with open("notes.txt","a") as f:
        f.write(report)

s=int(input("Enter the number of student"))
for i in range(s):
    st=str(input("Enter the student name"))
    stt=str(input("Enter the student status"))
    ts=time.time()
    attendance_checker(st,stt,ts)

print("Done")
