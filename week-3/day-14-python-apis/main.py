# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
# Adzuna needs two values, not one, so both are loaded here.
APP_ID = os.getenv("ADZUNA_APP_ID", "")
APP_KEY = os.getenv("ADZUNA_APP_KEY", "")
BASE_URL = "https://api.adzuna.com/v1/api/jobs/gb/search/1"


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": query,
        "where": "london",
        "results_per_page": 5,
    }

    try:
        response = requests.get(BASE_URL, params=params)
    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return None

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("The API request was not successful.")
        return None

    data = response.json()
    return data


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    results = data["results"]
    print("Total jobs found:", data["count"])
    print()

    for job in results:
        title = job["title"]
        company = job["company"]["display_name"]
        location = job["location"]["display_name"]

        print("Job Title:", title)
        print("Company:", company)
        print("Location:", location)
        print("-----")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()