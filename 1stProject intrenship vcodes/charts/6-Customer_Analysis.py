import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("transformed_retail_sales.csv")
print(df.shape)
print(df.columns.tolist())
# 1 — Customer Revenue 
# Calculate customer sales
customer_sales=df.groupby('Customer ID')['Sales'].sum()
print(customer_sales)
# Check number of customers
print('Total customers:',customer_sales.count())

# 2 — Top Customers 
# Find: Top 10 customers 
top_10_customers=customer_sales.sort_values(ascending=False).head(10)
print('Top 10 Customers')
print(top_10_customers)

# Find: Top 20 customers 
top_20_customers=customer_sales.sort_values(ascending=False).head(20)
print('Top 20 Customers')
print(top_20_customers)

# 3 — Average Customer Spending
total_customer_sales=customer_sales.sum()
number_of_customers=customer_sales.count()
average_customer_spending=total_customer_sales/number_of_customers

print('Total Customer Sales:',total_customer_sales)
print('Number of Customers:',number_of_customers)
print('Average of Customer Spending:',average_customer_spending)

# 4 — Repeat Customers
print('repeat customer vs one-time customer')
orders_per_customer=df.groupby('Customer ID')['Order ID'].nunique()
repeat_customers=orders_per_customer[orders_per_customer>1]
print('Repeat Customers:',repeat_customers.count())
one_time_customers=orders_per_customer[orders_per_customer==1]
print('One Time Customers:',one_time_customers.count())

# 5 — Customer Contribution
customer_contribution=(customer_sales/customer_sales.sum())*100
print('Customer Contribution:',customer_contribution)

# Top 10 contributors:
top_10_contribution=customer_contribution.sort_values(ascending=False)
print('Top 10 customer Contribution:')
print(top_10_contribution)

# 6 — Customer Segments
# High Value
# Medium Value
# Low Value
customer_segment=pd.qcut(
    customer_sales,
    q=3,
    labels=['Low Value','Medium Value','High Value']
    )
print('Customer_segment:',customer_segment.value_counts())

# 7 — Visualizations
# 1.Top 10 Customers
top_10_customers=customer_sales.sort_values(
    ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(
    top_10_customers.index,
    top_10_customers.values,
    color='skyblue',
    label='Customer Sales'
)
plt.title('Top 10 Customers by Sales')
plt.xlabel('Customer ID')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)#rotate the labels on the X-axis
plt.legend()
plt.show()

# Visualization 2: Customer Contribution
top_10_contribution=customer_contribution.sort_values(
    ascending=False).head(10)
plt.figure(figsize=(8, 8))

plt.pie(
    top_10_contribution.values,
    labels=top_10_contribution.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title('Top 10 customer-Revenue contribution')
plt.legend(title='Customer ID')

plt.show()

# Visualization 3 — Customer Segment Distribution
segment_counts=customer_segment.value_counts()
plt.figure(figsize=(8, 5))

plt.bar(
    segment_counts.index,
    segment_counts.values,
    color='steelblue',
    label='Number of Customers'
)

plt.title('Customer Segment Distribution')
plt.xlabel('Number Of Customers')
plt.ylabel('Customer Segment')
plt.legend()

plt.show()

# Visualization 4 — Repeat vs One-Time Customers
customer_type_counts={
    'Repeat Customers':repeat_customers.count(),
    'One-Time Customers':one_time_customers.count()
}

plt.figure(figsize=(7,7))

plt.pie(
    customer_type_counts.values(),
    labels=customer_type_counts.keys(),
    autopct="%1.1f%%",
    startangle=90,
      colors=["hotpink", "skyblue"],
     wedgeprops={"width": 0.4}#controls the thickness of the pie slices.
)

plt.title("Repeat vs One-Time Customers")
plt.legend(title='Customer Type')

plt.show()