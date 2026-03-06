import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_dataset.csv", encoding="utf-8-sig")

print("Original dataset shape:", df.shape)

# Remove rows with missing Customer ID
df = df.dropna(subset=["Customer ID"])

# Remove negative or zero quantity
df = df[df["Quantity"] > 0]

# Remove duplicate rows
df = df.drop_duplicates()

print("Cleaned dataset shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_retail.csv", index=False)

print("Cleaned dataset saved to data/cleaned_retail.csv")