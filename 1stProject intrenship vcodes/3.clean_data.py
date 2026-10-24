import pandas as pd
df=pd.read_csv('retail_sales.csv',encoding="latin1")
print('Raw data loaded successfully')
print('Rows:',len(df))
print('Columns:',len(df.columns))
# Fix Date Data Types
# Step 2: Convert date columns

df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed")

print("Date columns converted successfully")
print(df[["Order Date", "Ship Date"]].dtypes)
# 3.Remove Complete Duplicate Rows
before_rows=len(df)
df=df.drop_duplicates()
after_rows=len(df)
print('Duplicate rows  removed:',before_rows-after_rows)
print('Rows after cleaning:',after_rows)
# 4.Save the Cleaned CSV
df.to_csv('retail_sales.csv',index=False)
print('cleaned datset saved successfully')
# 5 — Final Verification
print('Final Rows:',len(df))
print('Final columns:',len(df.columns))
print('Missing values:',df.isnull().sum().sum())
print('Duplicate rows:',df.duplicated().sum())