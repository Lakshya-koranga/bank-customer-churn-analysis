"""
Bank Customer Churn Analysis
Author: Lakshya Koranga

Business question:
    Which customer segments have the highest churn risk, so the Retention Team
    can target them first?

Usage:
    python LakshyaKoranga_BankChurnAnalysis.py --data "Customer-Churn-Records.csv"

Outputs:
    - Printed summary tables (churn rate by segment)
    - Charts saved in the ./images folder
"""

import argparse
import os

import matplotlib
matplotlib.use("Agg")  # save charts to files without opening a window
import matplotlib.pyplot as plt
import pandas as pd

REQUIRED_COLUMNS = [
    "Geography", "Age", "NumOfProducts", "IsActiveMember", "Tenure", "Exited",
]


def load_data(path):
    """Load the CSV and check that the columns we need are present."""
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in the file: {missing}")
    return df


def add_age_group(df):
    """Create age bands: 18-27, 28-37, 38-47, 48-57, 58-67, 68+."""
    bins = [17, 27, 37, 47, 57, 67, 120]
    labels = ["18-27", "28-37", "38-47", "48-57", "58-67", "68+"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
    return df


def churn_by(df, column):
    """Return churn rate (%) and customer count for each value of `column`."""
    out = df.groupby(column, observed=True)["Exited"].agg(["count", "mean"])
    out["churn_rate_pct"] = (out["mean"] * 100).round(2)
    return out[["count", "churn_rate_pct"]]


def high_risk_segment(df):
    """Inactive customers in Germany aged 48-67."""
    mask = (
        (df["Geography"] == "Germany")
        & (df["IsActiveMember"] == 0)
        & (df["Age"].between(48, 67))
    )
    segment = df[mask]
    return len(segment), segment["Exited"].mean() * 100


def save_bar_chart(table, title, filename, folder):
    """Save a simple bar chart of churn rate by group."""
    os.makedirs(folder, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(table.index.astype(str), table["churn_rate_pct"], color="#2a78d6")
    ax.set_title(title)
    ax.set_ylabel("Churn rate (%)")
    for i, value in enumerate(table["churn_rate_pct"]):
        ax.text(i, value + 0.8, f"{value:.1f}%", ha="center", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(folder, filename), dpi=150)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Bank customer churn analysis")
    parser.add_argument("--data", default="Customer-Churn-Records.csv",
                        help="Path to the Kaggle Bank Customer Churn CSV file")
    parser.add_argument("--images", default="images", help="Folder for charts")
    args = parser.parse_args()

    df = add_age_group(load_data(args.data))

    total = len(df)
    churned = int(df["Exited"].sum())
    print(f"Customers: {total:,}")
    print(f"Churned:   {churned:,}")
    print(f"Overall churn rate: {df['Exited'].mean() * 100:.1f}%\n")

    analyses = [
        ("Geography", "Churn rate by country", "churn_by_country.png"),
        ("AgeGroup", "Churn rate by age group", "churn_by_age.png"),
        ("NumOfProducts", "Churn rate by number of products", "churn_by_products.png"),
        ("IsActiveMember", "Churn rate by activity (0 = inactive, 1 = active)", "churn_by_activity.png"),
        ("Tenure", "Churn rate by tenure (years)", "churn_by_tenure.png"),
    ]
    for column, title, filename in analyses:
        table = churn_by(df, column)
        print(f"--- {title} ---")
        print(table, "\n")
        save_bar_chart(table, title, filename, args.images)

    size, rate = high_risk_segment(df)
    print("--- High-risk segment ---")
    print("Inactive customers in Germany aged 48-67")
    print(f"Customers: {size}")
    print(f"Churn rate: {rate:.1f}%\n")

    if "Complain" in df.columns:
        print("--- Complaint check (possible data leakage) ---")
        print(churn_by(df, "Complain"))
        print("Complaints are almost perfectly linked to churn, so they were "
              "likely recorded at exit and are not used as a cause.")


if __name__ == "__main__":
    main()
