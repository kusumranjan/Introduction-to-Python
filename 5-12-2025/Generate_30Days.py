from datetime import date, timedelta

list = [(date.today() + timedelta(days=i)) for i in range(30)]
print(list)
