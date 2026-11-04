import os import requests

BASE_URL = "https://v3.football.api-sports.io"

def get_fixtures(date): api_key = os.getenv("API_FOOTBALL_KEY")

if not api_key:
    raise RuntimeError("Football API key is missing")

headers = {
    "x-apisports-key": api_key
}

params = {
    "date": date,
    "timezone": "Africa/Dar_es_Salaam"
}

response = requests.get(
    f"{BASE_URL}/fixtures",
    headers=headers,
    params=params,
    timeout=20
)

response.raise_for_status()

data = response.json()

if data.get("errors"):
    raise RuntimeError(f"Football API error: {data['errors']}")

return data.get("response", [])


def show_matches(date): matches = get_fixtures(date)

print("\nFOOTBALL MATCH ANALYSIS")

if not matches:
    print("No matches found.")
    return

for match in matches:
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]
    league = match["league"]["name"]
    kickoff = match["fixture"]["date"]

    print(f"\nLeague: {league}")
    print(f"Match: {home} vs {away}")
    print(f"Kickoff: {kickoff}")


if name == "main": from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
show_matches(today)
