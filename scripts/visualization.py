import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("database/retail.db")

print("Connected to database")

# 1️⃣ Monthly Sales Trend
monthly_sales = pd.read_sql("""
SELECT Month, SUM(TotalAmount) AS Revenue
FROM retail_sales
GROUP BY Month
ORDER BY Month
""", conn)

plt.figure(figsize=(8,5))
sns.lineplot(data=monthly_sales, x="Month", y="Revenue", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()


# 2️⃣ Top Selling Products
top_products = pd.read_sql("""
SELECT Description, SUM(Quantity) AS TotalSold
FROM retail_sales
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT 10
""", conn)

plt.figure(figsize=(10,5))
sns.barplot(data=top_products, x="TotalSold", y="Description")
plt.title("Top 10 Selling Products")
plt.show()


# 3️⃣ Revenue by Country
country_sales = pd.read_sql("""
SELECT Country, SUM(TotalAmount) AS Revenue
FROM retail_sales
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10
""", conn)

plt.figure(figsize=(10,5))
sns.barplot(data=country_sales, x="Revenue", y="Country")
plt.title("Top Countries by Revenue")
plt.show()


# 4️⃣ Quantity Distribution
quantity_data = pd.read_sql("SELECT Quantity FROM retail_sales", conn)

plt.figure(figsize=(8,5))
sns.histplot(quantity_data["Quantity"], bins=50)
plt.title("Quantity Distribution")
plt.show()


# 5️⃣ Outlier Detection (Boxplot)
plt.figure(figsize=(8,5))
sns.boxplot(x=quantity_data["Quantity"])
plt.title("Quantity Outliers")
plt.show()


# 6️⃣ Correlation Heatmap
data = pd.read_sql("""
SELECT Quantity, Price, TotalAmount, Month
FROM retail_sales
""", conn)

plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 7️⃣ Customer Purchase Frequency
customer_freq = pd.read_sql("""
SELECT `Customer ID`, COUNT(Invoice) AS PurchaseCount
FROM retail_sales
GROUP BY `Customer ID`
""", conn)

plt.figure(figsize=(8,5))
sns.histplot(customer_freq["PurchaseCount"], bins=50)
plt.title("Customer Purchase Frequency")
plt.show()


# Close connection
conn.close()