import pandas as pd
import os

def clean_data():
    file_path = "sensor_log.csv"
    
    if not os.path.exists(file_path):
        print("Error: No log file found to clean!")
        return

    # 1. Load the "dirty" data
    df = pd.read_csv(file_path)
    print(f"Original records: {len(df)}")

    # 2. Remove Duplicates (Clean)
    df_cleaned = df.drop_duplicates()
    
    # 3. Anomaly Detection (Logic)
    # If customer count > 80, we flag it as a 'High Traffic Event'
    df_cleaned['is_high_traffic'] = df_cleaned['customer_count'] > 80
    
    # 4. Save the professional version
    df_cleaned.to_csv("cleaned_sensor_data.csv", index=False)
    
    print(f"Cleaned records: {len(df_cleaned)}")
    print("✓ System: Duplicates removed and anomalies flagged.")
    print("✓ Result saved to: cleaned_sensor_data.csv")

if __name__ == "__main__":
    clean_data()