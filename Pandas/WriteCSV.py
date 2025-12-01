#Write csv
df.to_csv("students.csv",index=False)

print("csv file created")

#print(df)

df2 = df.copy()
df2.loc[2,"city"] = None
print(df2)
print(df2.isnull().sum())
df2_filled = df2.fillna("Unknown")
print(df2_filled)
