from datetime import datetime, date, time, timedelta

today=date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)

now=datetime.now()
print(now)

dob=date(1995,8,14)
print(dob)

now=datetime.now()
form=now.strftime("%d-%m-%y %H:%M:%S")
print(form) 


today=date.today()
next_week=today + timedelta(days=7)
yesterday=today - timedelta(days=1)
print(today)
print(next_week)
print(yesterday)

start=date(2024,1,1)
end=date(2024,12,31)
diff=end-start
print(diff.days)


dt=datetime.combine(date(2024,12,31),time(12,15,0))
print(dt)
