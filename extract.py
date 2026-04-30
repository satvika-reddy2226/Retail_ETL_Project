import pandas as pd
import sqlite3

# 1. Load the data (Matching your filenames exactly)
print("Loading CSV files...")
sales = pd.read_csv('sales data-set.csv')
stores = pd.read_csv('stores data-set.csv')
features = pd.read_csv('Features data set.csv')

# 2. Connect to SQL (This creates the database file)
conn = sqlite3.connect('retail_warehouse.db')

# 3. Save to SQL tables
print("Transferring data to SQL...")
sales.to_sql('sales', conn, if_exists='replace', index=False)
stores.to_sql('stores', conn, if_exists='replace', index=False)
features.to_sql('features', conn, if_exists='replace', index=False)

print("Project Step 1 Complete: 'retail_warehouse.db' created!")
conn.close()