# 4.Sales EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("transformed_retail_sales.csv")
print(df.head())
print('rows=',df.shape[0])
print('columns=',df.shape[1])
print(df.columns.tolist())
#1.Total Sales
total_sales=df['Sales'].sum()
print('Total Sales=',total_sales)
#2.Monthly Sales
monthly_sales=df.groupby('Month_Name')['Sales'].sum()
print('\nMonthly Sales:')
print(monthly_sales)

# arrange months in correct order
month_order=[
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
monthly_sales=monthly_sales.reindex(month_order)
print('\Monthly Sales in Correct Order')
print(monthly_sales)
# 2.1Create a monthly sales chart.
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index,monthly_sales.values,marker='*',color='hotpink')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
# plt.show()

#3.Category Sales
category_sales=df.groupby('Category')['Sales'].sum()
print('\nCategory Sales:')
print(category_sales)
# Category Sales Bar Chart
plt.figure(figsize=(8,5))
plt.bar(category_sales.index,category_sales.values,color='green')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/category_sales.png')
# plt.show()
# 4.calculate regional sales
regional_sales=df.groupby('Region')['Sales'].sum()
print('\nRegional Sales:')
print(regional_sales)
# Regional Sales Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(regional_sales.index,regional_sales.values)
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/region_sales.png')
# plt.show()
# 5 — Product Sales  Top 10 & Bottom 10 Products
product_sales=df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)
top_10_products=product_sales.head(10)
bottom_10_products=product_sales.tail(10)
print('\nTop 10 products')
print(top_10_products)
print('\nBottom 10 products')
print(bottom_10_products)

# Top 10 Products Chart


# Regional Sales Bar Chart

plt.figure(figsize=(8, 5))

plt.bar(regional_sales.index, regional_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("charts/region_sales.png")
# plt.show()


# Task 5 - Product Sales

product_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

top_10_products = product_sales.head(10)
bottom_10_products = product_sales.tail(10)

print("\nTop 10 Products:")
print(top_10_products)

print("\nBottom 10 Products:")
print(bottom_10_products)




# Top 10 Products Chart

plt.figure(figsize=(10, 6))
top_10_products.sort_values().plot(kind='barh')
plt.title('Top 10 products by sales')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.tight_layout()
plt.savefig('charts/top_products.png')
# plt.show()

# 6 — Profit Analysis
total_profit=df['Profit'].sum()
print('\nTotal Profit:',total_profit)
# Profit by Category
profit_category=df.groupby('Category')['Profit'].sum()
print('\nProfit by category')
print(profit_category)

# Profit by Category Chart

plt.figure(figsize=(8, 5))
plt.bar(profit_category.index,profit_category.values)
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("charts/profit_by_category.png")
plt.show()



# Profit by Category

profit_category = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(profit_category)


# Profit by Category Chart

plt.figure(figsize=(8, 5))

plt.bar(profit_category.index, profit_category.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("charts/profit_by_category.png")
plt.show()

# Profit by Region
profit_region=df.groupby('Region')['Profit'].sum()
print("\nProfit by Region:")
print(profit_region)

# Profit by Region Chart

plt.figure(figsize=(8, 5))

plt.bar(profit_region.index, profit_region.values)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("charts/profit_by_region.png")
plt.show()

# Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'],kde=True)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("charts/sales_distribution.png")
plt.show()