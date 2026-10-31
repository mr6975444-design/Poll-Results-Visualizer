
from src.cleaning import clean_data
from src.analysis import analyze_data

input_file = "data/raw/poll_data.csv"
output_file = "data/processed/cleaned_poll_data.csv"

# Step 1: Clean data
clean_data(input_file, output_file)

# Step 2: Analyse data
analyze_data(output_file)
