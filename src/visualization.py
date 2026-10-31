
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_charts(file_path):
    df = pd.read_csv(file_path)

    os.makedirs("outputs/charts", exist_ok=True)

    sns.set_theme(style="whitegrid")

    # Chart 1: Preferred Tool
    plt.figure(figsize=(9, 5))
    sns.countplot(
        data=df,
        x="Preferred Tool",
        order=df["Preferred Tool"].value_counts().index
    )
    plt.title("Most Preferred Programming Tools")
    plt.xlabel("Programming Tool")
    plt.ylabel("Number of Votes")
    plt.tight_layout()
    plt.savefig("outputs/charts/preferred_tools.png")
    plt.close()

    # Chart 2: Age Group Distribution
    plt.figure(figsize=(8, 5))
    df["Age Group"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Age Group Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/charts/age_distribution.png")
    plt.close()

    # Chart 3: Satisfaction Ratings
    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=df,
        x="Satisfaction",
        color="skyblue"
    )
    plt.title("Satisfaction Rating Distribution")
    plt.xlabel("Rating (1 to 5)")
    plt.ylabel("Number of Responses")
    plt.tight_layout()
    plt.savefig("outputs/charts/satisfaction.png")
    plt.close()

    print("All charts created successfully!")

if __name__ == "__main__":
    create_charts("data/processed/cleaned_poll_data.csv")
