import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv("sales_data.csv")
print("Data Preview:\n", df.head())

# 2. Total sales by product
print("\nTotal Sales by Product:")
print(df.groupby("Product")["Sales"].sum())

# 3. Total sales by region
print("\nTotal Sales by Region:")
print(df.groupby("Region")["Sales"].sum())

# 4. Draw charts
df.groupby("Product")["Sales"].sum().plot(kind="bar", title="Sales by Product")
plt.show()

df.groupby("Region")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.show()
