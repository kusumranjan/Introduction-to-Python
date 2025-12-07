from datetime import datetime, date, time, timedelta
start_date=input("Start date")
end_date=input("End date")
start_date=datetime.strptime(start_date,"%Y-%m-%d")
end_date=datetime.strptime(end_date,"%Y-%m-%d")
expiry_date=end_date - start_date
print(expiry_date.days)
