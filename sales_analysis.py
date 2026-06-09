import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales.csv")

# Show dataset
print("===== DATASET =====")
print(df)

# Basic statistics
print("\n===== STATISTICS =====")

print("Total Sales:")
print(df["Amount"].sum())

print("\nAverage Sale:")
print(df["Amount"].mean())

print("\nHighest Sale:")
print(df["Amount"].max())

print("\nLowest Sale:")
print(df["Amount"].min())

print("\nNumber of Records:")
print(len(df))

# Group by category
print("\n===== SALES BY CATEGORY =====")
print(df.groupby("Category")["Amount"].sum())

# Group by product
print("\n===== SALES BY PRODUCT =====")
print(df.groupby("Product")["Amount"].sum())

print("\nMedian Sale:")
print(df["Amount"].median())

print("\nCategory Count:")
print(df["Category"].value_counts())

print("\n===== ELECTRONICS =====")
print(df[df["Category"] == "Electronics"])

print("\n===== HIGH SALES =====")
print(df[df["Amount"] > 300])

print("\n===== SORTED SALES =====")
print(df.sort_values("Amount", ascending=False))

print("\n===== TOP 3 SALES =====")
print(df.nlargest(3, "Amount"))

df["Tax"] = df["Amount"] * 0.10

print("\n===== WITH TAX COLUMN =====")
print(df)

sales_by_category = df.groupby("Category")["Amount"].sum()

sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()

product_sales = df.groupby("Product")["Amount"].sum()

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.show()

df["Tax"] = df["Amount"] * 0.10
category_tax = df.groupby("Category")["Tax"].sum()

category_tax.plot(kind="bar")
plt.title("Category Tax")
plt.xlabel("Category")
plt.ylabel("Total Tax")
plt.show()