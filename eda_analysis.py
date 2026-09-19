import pandas as pd

df = pd.read_csv("../sales_cleaned.csv")

print(df.head())

# STEP 2 — Rows, Columns and Data Types check

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

#STEP 3 — Missing Values Check

print("\nMissing Values:")
print(df.isnull().sum())

# STEP 4 — Duplicate Records Check

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# STEP 5 — Basic Numerical Summary

print("\nNumerical Summary:")
print(df[["quantity", "sales", "discount"]].describe())

# STEP 6 — Category-wise Sales

print("\nSales by Category:")
print(df.groupby("category")["sales"].sum().sort_values(ascending=False))

# STEP 7 — State-wise Sales

print("\nSales by State:")
print(df.groupby("state")["sales"].sum().sort_values(ascending=False))

# STEP 8 — Top 5 Products by Sales

print("\nTop 5 Products by Sales:")
print(
    df.groupby("product")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# STEP 9 — Total Sales calculate 

print("\nTotal Sales:")
print(df["sales"].sum())

# STEP 10 — Average Sales calculate

print("\nAverage Sales:")
print(df["sales"].mean())

# STEP 11 — Total Quantity Sold

print("\nTotal Quantity Sold:")
print(df["quantity"].sum())

# STEP 12 — Highest Sales Order

print("\nHighest Sales Order:")
print(df.loc[df["sales"].idxmax()])

# STEP 13 — Monthly Sales Trend

print("\nMonthly Sales:")

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_sales = (
    df.groupby(df["order_date"].dt.month)["sales"]
    .sum()
    .sort_values(ascending=False)
)

print(monthly_sales)

# STEP 14 — Average Discount by Category

print("\nAverage Discount by Category:")
print(
    df.groupby("category")["discount"]
    .mean()
    .sort_values(ascending=False)
)

# STEP 15 — Sales vs Quantity

print("\nSales by Quantity:")
print(
    df.groupby("quantity")["sales"]
    .sum()
    .sort_values(ascending=False)
)

# Insight 1 — Category Performance

print("\nINSIGHT 1 - Highest Sales Category:")

category_sales = df.groupby("category")["sales"].sum()

highest_category = category_sales.idxmax()
highest_category_sales = category_sales.max()

print(f"{highest_category} has the highest total sales of ₹{highest_category_sales:,.2f}")

# Insight 2: Highest Sales State

print("\nINSIGHT 2 - Highest Sales State:")

state_sales = df.groupby("state")["sales"].sum()

highest_state = state_sales.idxmax()
highest_state_sales = state_sales.max()

print(f"{highest_state} has the highest total sales of ₹{highest_state_sales:,.2f}")

# Insight 3: Top-Selling Product

print("\nINSIGHT 3 - Top-Selling Product:")

product_sales = df.groupby("product")["sales"].sum()

top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

print(f"{top_product} has the highest total sales of ₹{top_product_sales:,.2f}")

# Insight 4: Highest Sales Month

print("\nINSIGHT 4 - Highest Sales Month:")

monthly_sales = df.groupby(df["order_date"].dt.month)["sales"].sum()

highest_month = monthly_sales.idxmax()
highest_month_sales = monthly_sales.max()

print(f"Month {highest_month} has the highest total sales of ₹{highest_month_sales:,.2f}")

# Insight 5: Highest Average Discount Category

print("\nINSIGHT 5 - Highest Average Discount Category:")

category_discount = (
    df[df["category"] != "Unknown"]
    .groupby("category")["discount"]
    .mean()
)

highest_discount_category = category_discount.idxmax()
highest_discount = category_discount.max()

print(f"{highest_discount_category} has the highest average discount of {highest_discount:.2%}")

