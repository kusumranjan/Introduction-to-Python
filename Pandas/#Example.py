import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45],
})
print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.describe())
#ex2
import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45],
})
print(df)
print(df["name"])
print(df[["name","marks"]])
high_scores=df[df["marks"]>70]
print(high_scores)
filtered=df[(df["marks"]>70) & (df["Age"]>22)]
print(filtered)
