from datetime import datetime


class WeatherParser:

    @staticmethod
    def parse_current(data: dict) -> dict:
        location = data["location"]
        current = data["current"]

        return {
            "city": location["name"],
            "country": location["country"],
            "temperature": current["temp_c"],
            "feels_like": current["feelslike_c"],
            "humidity": current["humidity"],
            "pressure": current["pressure_mb"],
            "wind_speed": current["wind_kph"],
            "description": current["condition"]["text"],
            "updated": current["last_updated"],
        }

    @staticmethod
    def parse_forecast(data: dict) -> list:
        forecast_days = data["forecast"]["forecastday"]
        forecast_list = []

        for day in forecast_days:
            forecast_list.append({
                "date": day["date"],
                "max_temp": day["day"]["maxtemp_c"],
                "min_temp": day["day"]["mintemp_c"],
                "description": day["day"]["condition"]["text"],
            })

        return forecast_list

    @staticmethod
    def to_fahrenheit(temp_c):
        return round((temp_c * 9/5) + 32, 2)
