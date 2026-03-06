import pandas as pd
import sqlite3

# Load transformed dataset
df = pd.read_csv("data/transformed_retail.csv")

print("Dataset loaded for database storage")

# Connect to SQLite database
conn = sqlite3.connect("database/retail.db")

# Store dataset in SQL table
df.to_sql("retail_sales", conn, if_exists="replace", index=False)

print("Data successfully stored in SQLite database")

# Close connection
conn.close()