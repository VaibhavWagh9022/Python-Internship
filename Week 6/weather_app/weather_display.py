from colorama import Fore, Style, init

init(autoreset=True)


class WeatherDisplay:

    @staticmethod
    def display_current(data: dict, unit="C"):
        temp = data["temperature"]

        if unit == "F":
            temp = round((temp * 9/5) + 32, 2)

        print("\n🌤 WEATHER DASHBOARD")
        print("=" * 30)
        print(f"📍 {data['city']}, {data['country']}")
        print(f"🕐 Updated: {data['updated']}\n")

        print(f"Temperature: {Fore.RED}{temp}°{unit}{Style.RESET_ALL}")
        print(f"Feels Like: {data['feels_like']}°C")
        print(f"Condition: {data['description']}")
        print(f"Humidity: {data['humidity']}%")
        print(f"Wind Speed: {data['wind_speed']} kph")
        print(f"Pressure: {data['pressure']} mb")

    @staticmethod
    def display_forecast(forecast: list):
        print("\n5-Day Forecast")
        print("-" * 30)

        for day in forecast:
            print(
                f"{day['date']} | "
                f"Max: {day['max_temp']}°C | "
                f"Min: {day['min_temp']}°C | "
                f"{day['description']}"
            )
