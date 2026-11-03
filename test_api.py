import os
import requests

API_KEY = os.getenv("API_FOOTBALL_KEY")

if not API_KEY:
    print("ERROR: API KEY haijaunganishwa!")
    exit()

url = "https://v3.football.api-sports.io/status"

headers = {
    "x-apisports-key": API_KEY
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    print("Status:", response.status_code)
    print("API Response:", response.json())

except Exception as error:
    print("Connection failed:", error)
