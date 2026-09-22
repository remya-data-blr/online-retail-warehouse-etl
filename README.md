# Online Retail ETL - From Raw to Warehouse

## What is this project?
Cleaned 541,909 messy retail transactions into a proper Data Warehouse using Python.

## Problem in Raw Data
- Cancelled orders starting with 'C'
- Null CustomerIDs
- Duplicates
- Negative Quantity & Zero Price
- No Total Amount column

## What I Did (ETL Steps)
**Extract:** Read 541k rows Excel file
**Transform:**
1. Filtered cancelled orders
2. Removed null customers
3. Removed duplicates
4. Fixed Quantity > 0 and Price > 0
5. Created Amount = Quantity * UnitPrice
6. Created IsCancelled flag

**Load:** Saved clean data to:
- `clean_retail.csv` (51 MB)

## Tech Used
- Python 3.9
- Pandas 1.5.3
- SQLite

## Result
BEFORE: 541,909 rows (messy)
AFTER: ~397k rows (clean) + Warehouse ready for SQL queries
