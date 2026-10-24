import pandas as pd
#            1.load dataset
df=pd.read_csv('retail_sales.csv',encoding="latin1")
#            2.Inspect Dataset
print(df.head()) # read top 5 records
print(df.tail()) # read last 5 records
print(df.shape) # gives number of rows and columns
print(df.columns) # gives columns name
print(df.info())# number of rows,column name,non null values
print(df.dtypes) # show datatypes
print(df.describe())#statistical summary of the numerical columns
print(df.nunique())#unique count of every column

#              3.Analyze Each Column 
print(df.isnull().sum())
print('duplicate value count')
print(df.duplicated().sum())
print("Missing Value Percentage:")
print((df.isnull().sum() / len(df)) * 100)

print("\nUnique Category Values:")
print(df["Category"].unique())

print('Unique Region Values')
print(df['Region'].unique())

print('Category Value Counts')
print(df['Category'].value_counts())

print('Region Value Counts')
print(df['Region'].value_counts())

print("Unique Values:")
print(df.nunique())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nExample Values:")
print(df.iloc[0])
