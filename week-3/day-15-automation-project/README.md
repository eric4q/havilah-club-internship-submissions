# Day 15 — Python Automation Project

## What does this project do?

<!-- Describe your project in 2-3 sentences. What problem does it solve? What does it automate? -->

This project reads a CSV file containing student names and scores, then
generates a formatted text report summarising the data — total number of
records, average score, highest score, and lowest score.

## Project Type

<!-- State which option you chose: File Organiser / Report Generator / Data Cleaner -->

Report Generator

## Requirements

<!-- List any Python libraries needed beyond the standard library -->

```
# example
pip install <library-name>
```
- Python 3.x
- No external packages required (uses only Python's standard library:
  os, csv)


## How to run

1. Make sure `data/students.csv` exists with `name,score` columns.
2. From inside this folder, run:

```bash
python main.py
```
3. The script will create `data/output/report.txt` automatically.

## Example output

<!-- Paste or screenshot the output your script produces when run on the sample data -->

Total Records: 8
Average Score: 69.125
Highest Score: 91
Lowest Score: 47