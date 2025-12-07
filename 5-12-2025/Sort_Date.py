
from datetime import datetime

dates = ["2025-01-10", "2024-12-31", "2025-01-01"]

converted = []
for d in dates:
    converted.append(datetime.strptime(d, "%Y-%m-%d"))

converted.sort()

print(converted)
