import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_retail.csv")

print("Dataset loaded for feature engineering")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True)

# Create TotalAmount column
df["TotalAmount"] = df["Quantity"] * df["Price"]

# Extract Month
df["Month"] = df["InvoiceDate"].dt.month

# Extract Day of Week
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

print("Feature engineering completed")

# Save transformed dataset
df.to_csv("data/transformed_retail.csv", index=False)

print("Transformed dataset saved as data/transformed_retail.csv")