import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("database/retail.db")

print("Connected to database")

# 1️⃣ Top 10 selling products
query1 = """
SELECT Description, SUM(Quantity) AS TotalSold
FROM retail_sales
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT 10
"""

top_products = pd.read_sql(query1, conn)

print("\nTop Selling Products:")
print(top_products)


# 2️⃣ Revenue by Country
query2 = """
SELECT Country, SUM(TotalAmount) AS Revenue
FROM retail_sales
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10
"""

country_sales = pd.read_sql(query2, conn)

print("\nTop Countries by Revenue:")
print(country_sales)


# 3️⃣ Monthly Sales Trend
query3 = """
SELECT Month, SUM(TotalAmount) AS MonthlyRevenue
FROM retail_sales
GROUP BY Month
ORDER BY Month
"""

monthly_sales = pd.read_sql(query3, conn)

print("\nMonthly Sales Trend:")
print(monthly_sales)


# 4️⃣ Customer Purchase Frequency
query4 = """
SELECT `Customer ID`, COUNT(Invoice) AS PurchaseCount
FROM retail_sales
GROUP BY `Customer ID`
ORDER BY PurchaseCount DESC
LIMIT 10
"""

top_customers = pd.read_sql(query4, conn)

print("\nTop Customers:")
print(top_customers)

# Close connection
conn.close()