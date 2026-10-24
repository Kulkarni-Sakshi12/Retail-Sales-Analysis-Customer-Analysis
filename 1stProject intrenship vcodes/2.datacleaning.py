import pandas as pd
df=pd.read_csv('retail_sales.csv',encoding="latin1")
# print(df.head())
# print(df.shape)
#1 check Missing Values.

print(df.isnull().sum())
print('Duplicate values sum')
print(df.duplicated().sum())
print(df.dtypes)
# 2.Fix Data Types
print('date conversion')
df['Order Date']=pd.to_datetime(df['Order Date'],format='mixed')
df['Ship Date']=pd.to_datetime(df['Ship Date'],format='mixed')
print(df.dtypes)
#3. Check Invalid Sales
print('check invalid sales')
print(df[df['Sales']<0])
# Standardize Categories
print('standardize categories')
print(df['Category'].unique())
#4 Validate Dates
print('count null dates')
print(df["Order Date"].isnull().sum())
print(df["Ship Date"].isnull().sum())
# 5.check for future dates.
from datetime import datetime
today=datetime.today()
print('Future order dates')
print(df[df['Order Date']>today])
print('Future ship dates')
print(df[df['Ship Date']>today])
# 6.check duplicate dates
print('Duplicate order Dates')
print(df['Order Date'].duplicated().sum())
print('Duplicate ship Dates')
print(df['Ship Date'].duplicated().sum())
print("Final rows:", len(df))
print("Final columns:", len(df.columns))