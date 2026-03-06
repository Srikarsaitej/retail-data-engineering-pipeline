import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_dataset.csv", encoding="utf-8-sig")

print("Dataset Loaded Successfully")
print(df.head())

print("Total rows:", len(df))
print("Columns:", df.columns)