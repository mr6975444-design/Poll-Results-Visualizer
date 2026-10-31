
import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    print("\n========== POLL ANALYSIS ==========")

    # Total responses
    print("\nTotal Responses:", len(df))

    # Preferred tool analysis
    print("\nPreferred Tool Votes:")
    print(df["Preferred Tool"].value_counts())

    # Most popular tool
    popular_tool = df["Preferred Tool"].mode()[0]
    print("\nMost Popular Tool:", popular_tool)

    # Age group analysis
    print("\nAge Group Distribution:")
    print(df["Age Group"].value_counts())

    # Satisfaction analysis
    average_rating = df["Satisfaction"].mean()
    print("\nAverage Satisfaction Rating:", round(average_rating, 2))

    # Feedback analysis
    print("\nFeedback Distribution:")
    print(df["Feedback"].value_counts())

    return df
