# 7 — Product Analysis
import pandas as pd
import matplotlib.pyplot as plt
# Load transformed dataset
df=pd.read_csv("transformed_retail_sales.csv")
print('Dataset Loaded Successfully!')
print('Rows:',df.shape[0])
print('Column:',df.shape[1])
print(df.head())
print(df.columns.tolist())

# 1 — Find the Top 10 Products by Sales
top_products=(
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print('\n Top 10 Products by Sales:')
print(top_products)

#visualization:Top 10 Products by Sales
plt.figure(figsize=(10,8))
top_products.sort_values().plot(
    kind='barh',
    color='seagreen'
)
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()

# 2: Find the Bottom 10 Products
bottom_products=(
   df.groupby('Product Name')['Sales']
  .sum().
   sort_values(ascending=True)#Lowest to highest.
   .head(10)
)
print('\Bottom 10 Products by Sales')
print(bottom_products)

# visualization bottom 10 products by sales
plt.figure(figsize=(8, 6))
bottom_products.sort_values(ascending=False).plot( #Highest to lowest.
    kind='barh',
    color='indianred'
)
plt.title('Bottom 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()

# 3.Calculate the Top 10 Most Profitable Products
profitable_products=(
  df.groupby('Product Name')['Profit']
  .sum()
  .sort_values(ascending=False)
  .head(10)
)

print('Top 10 Most Profitable Products')
print(profitable_products)

#visualization
plt.figure(figsize=(8,10))
profitable_products.plot(
    kind='bar',
    color='hotpink',
    edgecolor='black'
)
plt.title('Top 10 Most Profitable Products')
plt.xlabel('Product Name')
plt.ylabel('Total Profit')
plt.xticks(rotation=45,ha='right')#rotates product names to make them easier to read.
plt.tight_layout()#adjusts the spacing.
plt.show()

# 4.Calculate product-level sales, profit, and profit margin
# 4: HIGH SALES + LOW PROFIT MARGIN
product_analysis=df.groupby('Product Name').agg(  #.agg() stands for aggregation.
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
)
# Calculate profit margin percentage
product_analysis['Profit_Margin']=(
    product_analysis['Total_Profit']
    /product_analysis['Total_Sales']
)*100
print('\n PRODUCT SALES AND PROFIT MARGIN ')
print(product_analysis.head())

# Identify high-sales, low-margin products
# Select products with sales above the median
high_sales_limit=product_analysis['Total_Sales'].median()

# Select products with profit margin below the median
low_margin_limit=product_analysis['Profit_Margin'].median()
low_margin_products=product_analysis[
    (product_analysis['Total_Sales']>high_sales_limit)&
    (product_analysis['Profit_Margin']<low_margin_limit)
].sort_values('Total_Sales',ascending=False)
print("\n HIGH SALES + LOW PROFIT MARGIN PRODUCTS")
print(low_margin_products.head(10))

# Visualization: Sales vs Profit Margin
plt.figure(figsize=(10, 6))
plt.scatter(
    product_analysis['Total_Sales'],
    product_analysis['Profit_Margin'],
    color='skyblue',
    alpha=0.8
)
plt.axhline(                #horizontal line.
    low_margin_limit,
    color='red',
    linestyle='-.',
    label='Medium Profit Margin'
)

plt.axvline(             #  Draws a vertical line.
    high_sales_limit,
    color='blue',
    linestyle='--',
    label='Medium Sales'
)
plt.title("Product Sales vs Profit Margin")
plt.xlabel("Total Sales")
plt.ylabel("Profit Margin (%)")
plt.legend() 
plt.tight_layout()
plt.show()


# 5: Declining Products
# Convert Order Date to datetime format
df['Order Date']=pd.to_datetime(df['Order Date'])
# Create Year-Month column
df['Year_Month']=df['Order Date'].dt.to_period('M')
print("\n YEAR-MONTH DATA ")
print(df[["Order Date", "Year_Month"]].head())
# Calculate monthly sales for each product
monthly_product_sales=df.groupby(
    ['Year_Month','Product Name']
)['Sales'].sum().reset_index() #converts the grouped result into a regular DataFrame.
print("\n MONTHLY PRODUCT SALES ")
print(monthly_product_sales.head(10))
# Identify Products with Declining Sales#sort data by month
monthly_product_sales=monthly_product_sales.sort_values(#sort_values() arranges each product's sales by month, from the oldest
    ['Product Name','Year_Month']
)
# Check whether sales decrease from one month to the next
monthly_product_sales['Previous Month Sales']=(
    monthly_product_sales.groupby('Product Name')['Sales'].shift(1)#gets the product's sales from its previous recorded month.
)
monthly_product_sales['Sales Decreased']=(
    monthly_product_sales['Sales']
    <monthly_product_sales['Previous Month Sales']
)
print('\n Sales Decreased Check')
print(monthly_product_sales.head(10))

# Find products with sales decreasing in 3 consecutive comparisons
monthly_product_sales['Three_Month_Decline']=(
    monthly_product_sales.groupby('Product Name')['Sales Decreased']
    .transform(
        lambda x:x.rolling(3).sum().eq(3)
    )
)
declining_products=monthly_product_sales[
    monthly_product_sales['Three_Month_Decline']
]
print('\nPRODUCTS WITH CONSISTENTLY DECLINING SALES')
print(declining_products[['Product Name','Year_Month','Sales']].head(10))

#visualization
# Select the first 5 declining products
top_declining_names=declining_products['Product Name'].unique()[:5]
# Get monthly sales for these products
chart_data=monthly_product_sales[
    monthly_product_sales['Product Name'].isin(top_declining_names)
]#isin() checks whether a value is present in a list of values.
plt.figure(figsize=(12,6))
for product in top_declining_names:
    product_data=chart_data[
        chart_data['Product Name']==product
    ].sort_values('Year_Month')

    plt.plot(
        product_data['Year_Month'].astype(str),
        product_data['Sales'],
        marker='o',
        label=product
    )
plt.title("Monthly Sales Trend of Declining Products")
plt.xlabel("Year-Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend(fontsize=8)
plt.tight_layout()
plt.show()    

# 6: Category Performance Analysis.
category_performance=df.groupby('Category').agg(
    Total_Sales=('Sales','sum'),
    Total_Profit=('Profit','sum'),
    Total_Orders=('Order ID','nunique')#counts each different order only once.
)
# Calculate Profit Margin
category_performance['Profit_Margin']=(
    category_performance['Total_Profit']
    /category_performance['Total_Sales']
)*100
print('\nCategory Performance')
print(category_performance.round(2))

# Visualization 1: Sales by Category
plt.figure(figsize=(9, 5))
category_performance['Total_Sales'].plot(
    kind='bar',
    color='teal',
    edgecolor='black'
)
plt.title("Total Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualization 2: Profit by Category
plt.figure(figsize=(9, 5))
category_performance['Total_Profit'].plot(
    kind='bar',
    color="mediumseagreen",
    edgecolor='black'
)

plt.title("Total Profit by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualization 3: Profit Margin by Category
plt.figure(figsize=(9, 5))
category_performance['Profit_Margin'].plot(
    kind='bar',
    color='darkorange',
    edgecolor='black'
)
plt.title('Profit Margin by Category')
plt.xlabel('Product Category')
plt.ylabel('Profit Margin(%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualization 4: Total Orders by Category
plt.figure(figsize=(9, 5))

category_performance["Total_Orders"].plot(
    kind="bar",
    color="mediumpurple",
    edgecolor="black"
)
plt.title("Total Orders by Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Visualization 5: Sales vs Profit by Category

category_performance[["Total_Sales", "Total_Profit"]].plot(
    kind="bar",
    figsize=(10, 6),
    edgecolor="black"
)

plt.title("Sales vs Profit by Category")
plt.xlabel("Product Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.legend(["Total Sales", "Total Profit"])
plt.tight_layout()
plt.show()

# TASK 7: EXPORT PRODUCT PERFORMANCE REPORT

product_analysis.to_csv("Product_Performance.csv")

print("Product Performance CSV saved successfully!")