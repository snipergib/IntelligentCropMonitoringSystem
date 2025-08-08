import pandas as pd
import psycopg2

def load_csv_to_postgres(csv_path):
    df = pd.read_csv(csv_path)

    # ✅ PostgreSQL connection setup for Supabase
    conn = psycopg2.connect(
        host="SUPABASE-LINK",
        port="YOUR-PORT-NO",
        database="postgres",
        user="POSTGRES-NAME",
        password="POSTGRES-PASSWORD",  # 🔐 Consider using environment variables
        sslmode="require"      # ✅ Required for Supabase
    )

    cur = conn.cursor()

    # ✅ Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS crop_recommendation (
            nitrogen INTEGER,
            phosphorus INTEGER,
            potassium INTEGER,
            temperature FLOAT,
            humidity FLOAT,
            pH_value FLOAT,
            rainfall FLOAT,
            crop VARCHAR(50)
        )
    """)

    # ✅ Insert each row
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO crop_recommendation (
                nitrogen, phosphorus, potassium,
                temperature, humidity, pH_value,
                rainfall, crop
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Nitrogen'],
            row['Phosphorus'],
            row['Potassium'],
            row['Temperature'],
            row['Humidity'],
            row['pH_Value'],
            row['Rainfall'],
            row['Crop']
        ))

    conn.commit()
    cur.close()
    conn.close()


    print("✅ Data inserted successfully into PostgreSQL.")
