import pandas as pd
import sqlite3

# Your path from your screenshot - perfect!
df = pd.read_excel("online_retail_data_lake/Raw/Online Retail.xlsx")
print(f"RAW: {df.shape}")

df = df[~df['Description'].isna()]
df = df[df['UnitPrice'] > 0]
df['CustomerID'] = df['CustomerID'].fillna(0).astype(int)
df['IsCancelled'] = df['InvoiceNo'].astype(str).str.startswith('C').astype(int)
df['Amount'] = (df['Quantity'] * df['UnitPrice']).round(2)

df.to_csv("online_retail_data_lake/Clean/online_retail_clean.csv", index=False)

conn = sqlite3.connect("online_retail_warehouse.db")
df.to_sql("fact_retail", conn, if_exists="replace", index=False)
conn.close()
print(f"CLEAN: {df.shape} -> DB Created!")
df.head(20).to_csv("sample_data.csv", index=False)