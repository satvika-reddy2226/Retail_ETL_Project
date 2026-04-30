import pandas as pd
from datetime import datetime
import random
import os

def simulate_api_call():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Connecting to Simulated Data Stream...")
    
    # 1. Simulating the data we would get from a real API
    # Imagine these are real-time readings from a retail store's smart sensors
    simulated_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'store_id': random.randint(1, 50),
        'customer_count': random.randint(10, 100),
        'temp_celsius': round(random.uniform(15.0, 35.0), 2),
        'status': 'Online'
    }
    
    print(f"✓ Success! Data received from Store {simulated_data['store_id']}")
    print(f"✓ Current Customer Count: {simulated_data['customer_count']}")
    
    # 2. Save to a CSV (The 'Pipeline' part)
    df = pd.DataFrame([simulated_data])
    file_exists = os.path.isfile("sensor_log.csv")
    df.to_csv("sensor_log.csv", mode='a', index=False, header=not file_exists)
    print("✓ Data logged to sensor_log.csv")

if __name__ == "__main__":
    simulate_api_call()