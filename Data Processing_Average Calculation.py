import os
import matplotlib.pyplot as plt
import pandas as pd

# Constants
DATASET_PATH = "student_scores.csv"

def create_sample_dataset():
    """Creates the student scores dataset if it doesn't already exist."""
    data = [
        ["student_id", "name", "subject", "score"],
        [1, "Alice Smith", "Math", 88],
        [2, "Bob Jones", "Math", 76],
        [3, "Charlie Brown", "Math", 92],
        [4, "Diana Prince", "Math", 81],
        [5, "Ethan Hunt", "Math", 95],
        [6, "Fiona Glenanne", "Math", 84]
    ]
    import csv
    with open(DATASET_PATH, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def process_and_visualize_dataset():
    """Loads the dataset, calculates statistics, and visualizes student scores."""
    # Ensure the dataset file exists
    if not os.path.exists(DATASET_PATH):
        create_sample_dataset()

    # Load the dataset using Pandas
    df = pd.read_csv(DATASET_PATH)
    print(f"Successfully loaded dataset from '{DATASET_PATH}' with {len(df)} records.")

    # Calculate the average score
    average_score = df["score"].mean()
    print(f"Class Average Test Score: {average_score:.2f}")

    # Create Bar Chart Visualization
    plt.figure(figsize=(9, 5))
    plt.bar(df["name"], df["score"], color="skyblue", edgecolor="navy", width=0.6)
    
    # Add a horizontal dashed line for the average score
    plt.axhline(average_score, color="red", linestyle="dashed", linewidth=1.5, label=f"Average Score: {average_score:.1f}")
    
    # Formatting the chart
    plt.title("Student Test Scores Analysis", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Student Name", fontsize=12)
    plt.ylabel("Test Score", fontsize=12)
    plt.ylim(0, 100)
    plt.legend(loc="upper right")
    
    # Fixed grid line style
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    plt.xticks(rotation=15)
    plt.tight_layout()
    
    # Save chart as image file
    chart_path = "student_scores_bar_chart.png"
    plt.savefig(chart_path)
    print(f"Bar chart visualization successfully saved to '{chart_path}'")
    
    # Display the plot window
    plt.show()

if __name__ == "__main__":
    process_and_visualize_dataset()