import csv_loader
import data_cleaning

RAW_CSV = "crop_data.csv"
CLEAN_CSV = "transformed_crop_data.csv"

# Clean + transform
data_cleaning.clean_and_transform(RAW_CSV, CLEAN_CSV)

# Load to DB
csv_loader.load_csv_to_postgres(CLEAN_CSV)