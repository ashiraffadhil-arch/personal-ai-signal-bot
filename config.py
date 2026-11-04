import os

Application settings

APP_NAME = "PERSONAL AI SIGNAL BOT" APP_VERSION = "1.0.0"

Football API configuration

API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY") API_FOOTBALL_URL = "https://v3.football.api-sports.io"

Timezone

TIMEZONE = "Africa/Dar_es_Salaam"

Database configuration

DATABASE_NAME = "signals.db"

def validate_config(): print(f"{APP_NAME} v{APP_VERSION}") print("Configuration loaded successfully.")

if not API_FOOTBALL_KEY:
    print("WARNING: Football API key is not configured.")
else:
    print("Football API key detected.")
