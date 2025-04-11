import time
import random
import pandas as pd
from database import engine

def generate_sensor_data():
    return {
        "sensor_id": random.randint(100, 200),
        "soil_moisture": round(random.uniform(20.0, 40.0), 2),
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 90.0), 2),
        "timestamp": pd.Timestamp.now()
    }

def insert_to_postgres(data):
    df = pd.DataFrame([data])
    df.to_sql("sensor_readings", engine, if_exists="append", index=False)
    print("✅ Inserted:", data)

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        insert_to_postgres(sensor_data)
        time.sleep(5)  # Simulate data every 5 seconds