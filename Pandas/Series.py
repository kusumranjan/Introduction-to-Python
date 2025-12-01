import pandas as pd

# Series
s = pd.Series([10, 20, 30, 40])
print(s)

# DataFrame
data = {
    "Name": ["Aisha", "Rahul", "John"],
    "Marks": [100, 80, 90]
}

df = pd.DataFrame(data)
print(df)
