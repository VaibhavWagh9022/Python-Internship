import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict
from .config import BASE_URL, API_KEY, CACHE_DIR, CACHE_DURATION


class WeatherAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL

    def _cache_file(self, key: str) -> Path:
        return CACHE_DIR / f"{key}.json"

    def _get_cached(self, key: str) -> Optional[Dict]:
        file = self._cache_file(key)
        if file.exists():
            if time.time() - file.stat().st_mtime < CACHE_DURATION:
                with open(file, "r") as f:
                    return json.load(f)
        return None

    def _save_cache(self, key: str, data: Dict):
        with open(self._cache_file(key), "w") as f:
            json.dump(data, f, indent=2)

    def _request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params["key"] = self.api_key

            response = requests.get(
                f"{self.base_url}/{endpoint}",
                params=params,
                timeout=10,
            )

            if response.status_code == 200:
                return response.json()
            else:
                print("API Error:", response.json())
                return None

        except requests.exceptions.RequestException as e:
            print("Network Error:", e)
            return None

    def get_current_weather(self, city: str) -> Optional[Dict]:
        cache_key = f"current_{city.lower()}"
        cached = self._get_cached(cache_key)
        if cached:
            return cached

        data = self._request("current.json", {"q": city})
        if data:
            self._save_cache(cache_key, data)
        return data

    def get_forecast(self, city: str) -> Optional[Dict]:
        cache_key = f"forecast_{city.lower()}"
        cached = self._get_cached(cache_key)
        if cached:
            return cached

        data = self._request("forecast.json", {"q": city, "days": 5})
        if data:
            self._save_cache(cache_key, data)
        return data
