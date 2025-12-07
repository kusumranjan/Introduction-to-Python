from datetime import datetime

timestamps = [
    "2025-12-01 09:00",
    "2025-12-02 09:05",
    "2025-12-03 09:10",
    "2025-12-04 09:15",
    "2025-12-05 09:20",
    "2025-12-06 09:25",
    "2025-12-07 09:30",
    "2025-12-08 09:35",
    "2025-12-09 09:40",
    "2025-12-10 09:45"
]
c=0
for i in timestamps:
    s=datetime.strptime(i,"%Y-%m-%d %H:%M").weekday()
    if s==0:
        c+=1

print(c)
