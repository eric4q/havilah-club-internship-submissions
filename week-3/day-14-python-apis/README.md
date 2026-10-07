# Day 14 - Python + APIs

Connects to the Adzuna job search API to retrieve live job listings.

## API
- Provider: Adzuna (https://developer.adzuna.com)
- Endpoint: https://api.adzuna.com/v1/api/jobs/gb/search/1
- Auth: app_id and app_key passed as query parameters (see .env.example)
- Parameters used: what (job title keyword), where (location), results_per_page

## What it does
Sends a GET request for "python developer" jobs in "london", checks the
response status, and prints the title, company, and location for each
result found.

## Run it
pip install -r requirements.txt   (or: pip install requests python-dotenv)
Create a .env file with ADZUNA_APP_ID and ADZUNA_APP_KEY (see .env.example)
python main.py