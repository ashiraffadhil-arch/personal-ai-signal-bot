import os
import requests

API_KEY = os.getenv("API_FOOTBALL_KEY")

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_fixtures(date):
    url = f"{BASE_URL}/fixtures"

    params = {
        "date": date,
        "timezone": "Africa/Dar_es_Salaam"
    }

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=20
        )

        response.raise_for_status()
        data = response.json()

        if data.get("errors"):
            print("API error:", data["errors"])
            return []

        return data.get("response", [])

    except requests.RequestException as error:
        print("Connection error:", error)
        return []


def show_matches(date):
    matches = get_fixtures(date)

    print("\n⚽ FOOTBALL MATCHES")

    if not matches:
        print("Hakuna mechi zilizopatikana.")
        return

    for match in matches:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]
        league = match["league"]["name"]
        time = match["fixture"]["date"]

        print(f"\n{league}")
        print(f"{home} vs {away}")
        print(f"Time: {time}")


if __name__ == "__main__":
    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")
    show_matches(today)
