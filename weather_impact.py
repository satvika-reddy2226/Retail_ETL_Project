import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('retail_warehouse.db')

# This query joins Sales and Features to see if Temperature affects Weekly_Sales
query = """
SELECT f.Temperature, s.Weekly_Sales
FROM sales s
JOIN features f ON s.Store = f.Store AND s.Date = f.Date
"""

df = pd.read_sql(query, conn)

# Create a Scatter Plot to see the relationship
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Weekly_Sales'], alpha=0.1, color='orange')
plt.title('Impact of Temperature on Weekly Sales')
plt.xlabel('Temperature (Fahrenheit)')
plt.ylabel('Weekly Sales')
plt.grid(True)
plt.show()

conn.close()