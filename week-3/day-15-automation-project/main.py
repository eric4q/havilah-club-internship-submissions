# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser   — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner      — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
import csv
# import shutil  # uncomment if using File Organiser

# ── Configuration ──────────────────────────────────────────────────────────────
# Set your input/output paths here so they are easy to find and change.

INPUT_PATH = "data/"
OUTPUT_PATH = "data/output/"


# ── Core Functions ────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def load_students(input_path):
    filepath = input_path + "students.csv"

    try:
        file = open(filepath, "r")
    except FileNotFoundError:
        print("Input file not found:", filepath)
        return []

    rows = []
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)
    file.close()

    return rows


def calculate_summary(rows):
    scores = []

    for row in rows:
        try:
            score_value = int(row["score"])
            scores.append(score_value)
        except ValueError:
            print("Skipping row with invalid score:", row)

    if len(scores) == 0:
        print("No valid scores found.")
        return None

    summary = {
        "total_records": len(scores),
        "average_score": sum(scores) / len(scores),
        "highest_score": max(scores),
        "lowest_score": min(scores),
    }

    return summary


def write_report(summary, output_path):
    if summary is None:
        print("No summary to write.")
        return

    os.makedirs(output_path, exist_ok=True)
    filepath = output_path + "report.txt"

    file = open(filepath, "w")
    file.write("Student Score Report\n")
    file.write("=====================\n")
    file.write("Total Records: " + str(summary["total_records"]) + "\n")
    file.write("Average Score: " + str(summary["average_score"]) + "\n")
    file.write("Highest Score: " + str(summary["highest_score"]) + "\n")
    file.write("Lowest Score: " + str(summary["lowest_score"]) + "\n")
    file.close()

    print("Report written to:", filepath)


def process(input_path, output_path):
    rows = load_students(input_path)

    if len(rows) == 0:
        print("No data to process.")
        return

    summary = calculate_summary(rows)
    write_report(summary, output_path)


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()