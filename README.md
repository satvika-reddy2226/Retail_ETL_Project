# Retail Data ETL & Analytics Pipeline

A professional end-to-end data engineering project that automates the transition of raw retail data into an actionable SQL warehouse.

## 🚀 Project Overview
This project demonstrates a full ETL (Extract, Transform, Load) lifecycle. It processes over 400,000 rows of retail data (Sales, Stores, and Features) to identify business-critical trends and performance metrics.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Libraries:** Pandas (Data Manipulation), Matplotlib (Visualization)
- **Database:** SQLite3 (SQL Warehouse)
- **Version Control:** Git & GitHub

## 📊 Key Insights
- **Top Performers:** Identified Store 20 as the leading revenue driver with over 300M in total sales.
- **Weather Analysis:** Performed correlation testing between temperature and weekly sales to determine environmental impacts on retail performance.
- **Automation:** Built a reusable pipeline that can ingest updated CSV files and refresh the SQL database in seconds.

## 📁 File Structure
- `extract.py`: The ETL engine that builds the SQL warehouse.
- `analysis.py`: Generates the Top 10 Stores bar chart.
- `weather_impact.py`: Performs correlation analysis between external features and revenue.
- `retail_warehouse.db`: The structured relational database.

## ⚙️ How to Run
1. Install dependencies:
   ```powershell
   pip install pandas matplotlib