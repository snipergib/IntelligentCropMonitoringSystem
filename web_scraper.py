import pandas as pd

# Simulated crop dataset for loading into PostgreSQL
data = {
    "crop_name": ["Wheat", "Rice", "Maize", "Barley", "Soybean"],
    "soil_type": ["Loamy", "Clay", "Sandy", "Silty", "Peaty"],
    "avg_temp_celsius": [20.5, 25.2, 22.8, 18.0, 21.3],
    "avg_rainfall_mm": [400, 1200, 600, 300, 800],
    "fertilizer_used": ["Urea", "DAP", "MOP", "NPK", "Compost"],
    "irrigation_required": ["Yes", "Yes", "No", "No", "Yes"],
    "yield_per_hectare_kg": [3500, 5000, 4000, 2800, 3200]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_path = "/mnt/data/crop_data.csv"
df.to_csv(csv_path, index=False)

csv_path