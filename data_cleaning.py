import pandas as pd

# Load dataset
df = pd.read_csv("dirty_sales.csv")

print("===== ORIGINAL DATASET =====")
print(df)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull())

# Count missing values per column
print("\n===== MISSING VALUE COUNT =====")
print(df.isnull().sum())

# Calculate average amount
average_amount = df["Amount"].mean()

print("\nAverage Amount:")
print(average_amount)

# Replace missing values with average
df["Amount"] = df["Amount"].fillna(average_amount)

print("\n===== CLEANED DATASET =====")
print(df)

# Verify missing values are gone
print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())