
import pandas as pd

def clean_data(input_file, output_file):
    # Load raw poll data
    df = pd.read_csv(input_file)

    print("Original data shape:", df.shape)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna(subset=["Preferred Tool", "Satisfaction"])

    # Convert Timestamp to datetime
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    # Remove rows with invalid timestamps
    df = df.dropna(subset=["Timestamp"])

    # Save cleaned data
    df.to_csv(output_file, index=False)

    print("Data cleaning completed!")
    print("Cleaned data shape:", df.shape)
    print("Saved cleaned data to:", output_file)

    return df
