# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    # TODO: open the file and read rows into the list
    file = open(filepath, "r")
    reader = csv.DictReader(file)
 
    for row in reader:
        row["name"] = row["name"].strip()
        row["score"] = int(row["score"])
        rows.append(row)
 
    file.close()
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    # TODO: implement summary statistics
    total_rows = len(rows)
 
    scores = []
    for row in rows:
        scores.append(row["score"])
 
    minimum_score = min(scores)
    maximum_score = max(scores)
    average_score = sum(scores) / len(scores)
 
    print("Total Records:", total_rows)
    print("Minimum Score:", minimum_score)
    print("Maximum Score:", maximum_score)
    print("Average Score:", average_score)


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    # TODO: define and apply your filter condition
    for row in rows:
        if row["score"] > 70:
            filtered.append(row)
    return filtered

def get_score(row):
    return row["score"]


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    # TODO: sort rows by a column, then write to CSV
    sorted_rows = sorted(rows, key=get_score)
 
    file = open(filepath, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=["name", "score", "grade"])
    writer.writeheader()
 
    for row in sorted_rows:
        writer.writerow(row)
 
    file.close()


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
