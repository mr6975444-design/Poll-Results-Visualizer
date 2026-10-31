
import pandas as pd
import numpy as np
import os

# Make sample data reproducible
np.random.seed(42)

# Number of survey responses
num_responses = 200

# Generate sample poll data
data = {
    "Timestamp": pd.date_range(
        start="2026-01-01",
        periods=num_responses,
        freq="h"
    ),
    "Age Group": np.random.choice(
        ["18-25", "26-35", "36-45", "46+"],
        num_responses
    ),
    "Gender": np.random.choice(
        ["Female", "Male", "Other"],
        num_responses
    ),
    "Preferred Tool": np.random.choice(
        ["Python", "Java", "C++", "JavaScript", "SQL"],
        num_responses
    ),
    "Satisfaction": np.random.randint(
        1, 6, num_responses
    ),
    "Feedback": np.random.choice(
        [
            "Easy to use",
            "Very useful",
            "Needs improvement",
            "Good experience",
            "Excellent tool"
        ],
        num_responses
    )
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create output folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Save data as CSV
df.to_csv("data/raw/poll_data.csv", index=False)

print("Sample poll data generated successfully!")
print(df.head())
print(f"\nTotal responses: {len(df)}")
