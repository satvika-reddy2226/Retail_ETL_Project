import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('retail_warehouse.db')

query = """
SELECT Store, SUM(Weekly_Sales) as Total_Sales
FROM sales
GROUP BY Store
ORDER BY Total_Sales DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

# Create the Chart
plt.figure(figsize=(10, 6))
plt.bar(df['Store'].astype(str), df['Total_Sales'], color='skyblue')
plt.xlabel('Store Number')
plt.ylabel('Total Sales (in 100 Millions)')
plt.title('Top 10 Stores by Total Sales')
plt.show()

conn.close()