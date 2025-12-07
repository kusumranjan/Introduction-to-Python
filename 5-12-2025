from datetime import date, timedelta

expiry_dates = [date(2025, 12, 6), date(2025, 12, 12), date(2025, 12, 25)]
today = date.today()
limit = today + timedelta(days=15)

near_expiry = [d for d in expiry_dates if today <= d <= limit]
print(near_expiry)
