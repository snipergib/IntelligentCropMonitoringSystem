import pandas as pd

def clean_and_transform(input_path, output_path):
    df = pd.read_csv(input_path)

    print("🔍 Original Data Preview:")
    print(df.head())

    # ======== DATA CLEANING ========

    # Drop rows with any missing critical values
    df.dropna(subset=[
        'Nitrogen', 'Phosphorus', 'Potassium',
        'Temperature', 'Humidity', 'pH_Value',
        'Rainfall', 'Crop'
    ], inplace=True)

    # Standardize crop name formatting
    df['Crop'] = df['Crop'].str.strip().str.title()

    # Remove duplicates
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)

    # ======== DATA TRANSFORMATION ========

    # Categorize yield potential based on nutrient richness (mock logic)
    def nutrient_score(row):
        return row['Nitrogen'] + row['Phosphorus'] + row['Potassium']

    df['nutrient_score'] = df.apply(nutrient_score, axis=1)
    df['yield_category'] = pd.cut(
        df['nutrient_score'],
        bins=[0, 150, 250, 400],
        labels=['Low', 'Medium', 'High']
    )

    # Temperature category
    df['temp_category'] = pd.cut(
        df['Temperature'],
        bins=[0, 15, 25, 40],
        labels=['Low', 'Moderate', 'High']
    )

    # Rainfall category
    df['rainfall_category'] = pd.cut(
        df['Rainfall'],
        bins=[0, 100, 200, 300],
        labels=['Low', 'Medium', 'High']
    )

    # Save cleaned and transformed data
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned & transformed data saved to {output_path}")


# Example usage
if __name__ == "__main__":
    clean_and_transform("Crop_Recommendation.csv", "transformed_crop_data.csv")