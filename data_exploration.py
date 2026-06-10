import pandas as pd

df = pd.read_csv('sales.csv')

print(df)

# print first 2 lines
print(df.head(2))

print(df.tail(2))

print(df.info())

print(df.describe())

print(df.columns)

print(df["Category"].unique())

print(df["Category"].nunique())

print(df["Category"].value_counts())

print("Products:")
print(df["Product"].unique())

print("Number of Products:")
print(df["Product"].nunique())
