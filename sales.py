
# Retail Sales Data Analysis
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create Sample Dataset


np.random.seed(10)

products = ["Laptop","Mobile","Shoes","Shirt","Table","Chair"]
categories = ["Electronics","Electronics","Fashion","Fashion","Furniture","Furniture"]
prices = [70000,30000,3500,1200,9000,3500]

n = 500

df = pd.DataFrame({
    "Product":np.random.choice(products,n),
    "Quantity":np.random.randint(1,8,n),
    "Region":np.random.choice(["North","South","East","West"],n),
    "Month":np.random.choice(["Jan","Feb","Mar","Apr","May","Jun",
                              "Jul","Aug","Sep","Oct","Nov","Dec"],n)
})

price_dict=dict(zip(products,prices))
category_dict=dict(zip(products,categories))

df["UnitPrice"]=df["Product"].map(price_dict)
df["Category"]=df["Product"].map(category_dict)

df["Revenue"]=df["Quantity"]*df["UnitPrice"]

# Add Missing Values & Duplicates


df.loc[10,"Quantity"]=np.nan
df.loc[25,"Region"]=np.nan

df=pd.concat([df,df.iloc[0:5]],ignore_index=True)


# Data Cleaning


print("Shape :",df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows :",df.duplicated().sum())

df.drop_duplicates(inplace=True)

df["Quantity"].fillna(df["Quantity"].median(),inplace=True)
df["Region"].fillna(df["Region"].mode()[0],inplace=True)

df["Quantity"]=df["Quantity"].astype(int)

print("\nAfter Cleaning")
print(df.isnull().sum())


# Basic Information


print("\nDataset Info")
print(df.info())

print("\nStatistics")
print(df.describe())


# Monthly Revenue


monthly_sales=df.groupby("Month")["Revenue"].sum()

month_order=["Jan","Feb","Mar","Apr","May","Jun",
             "Jul","Aug","Sep","Oct","Nov","Dec"]

monthly_sales=monthly_sales.reindex(month_order)


# Category Revenue


category_sales=df.groupby("Category")["Revenue"].sum()


# Region Revenue


region_sales=df.groupby("Region")["Revenue"].sum()


# Top Products


top_products=(df.groupby("Product")["Revenue"]
                .sum()
                .sort_values(ascending=False))

print("\nTop Products")
print(top_products)


# Total Revenue


print("\nTotal Revenue : ₹",df["Revenue"].sum())

print("Average Order Value : ₹",round(df["Revenue"].mean(),2))

print("Best Category :",category_sales.idxmax())

print("Best Region :",region_sales.idxmax())


# Graph 1
# Monthly Revenue


plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# Graph 2
# Category Revenue


plt.figure(figsize=(6,5))
category_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.show()

# Graph 3
# Region Revenue


plt.figure(figsize=(6,5))
region_sales.plot(kind="bar",color="orange")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.show()


# Graph 4
# Top Products


plt.figure(figsize=(7,5))
top_products.plot(kind="bar")
plt.title("Top Products by Revenue")
plt.ylabel("Revenue")
plt.show()

# Business Insights


print("\nBusiness Insights")

print("- Highest revenue category :",category_sales.idxmax())

print("- Highest revenue region :",region_sales.idxmax())

print("- Best selling product :",top_products.idxmax())

print("- Total Revenue :",df["Revenue"].sum())

print("- Average Revenue per Order :",round(df["Revenue"].mean(),2))