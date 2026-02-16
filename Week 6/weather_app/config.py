import os
from dotenv import load_dotenv
from pathlib import Path

# Force load .env from root directory
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

BASE_URL = "http://api.weatherapi.com/v1"
API_KEY = os.getenv("API_KEY")

CACHE_DIR = Path("data/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

CACHE_DURATION = 600

FAVORITES_FILE = Path("data/favorites.json")
