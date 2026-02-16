import json
from .weather_api import WeatherAPI
from .weather_parser import WeatherParser
from .weather_display import WeatherDisplay
from .config import FAVORITES_FILE


class WeatherApp:

    def __init__(self):
        self.api = WeatherAPI()
        self.unit = "C"

    def run(self):
        while True:
            command = input("\nEnter city (or help/quit/favorites): ").strip()

            if command.lower() == "quit":
                print("Goodbye!")
                break

            elif command.lower() == "help":
                self.show_help()

            elif command.lower() == "favorites":
                self.show_favorites()

            else:
                self.show_weather(command)

    def show_weather(self, city):
        current = self.api.get_current_weather(city)
        forecast = self.api.get_forecast(city)

        if current:
            parsed_current = WeatherParser.parse_current(current)
            WeatherDisplay.display_current(parsed_current, self.unit)

        if forecast:
            parsed_forecast = WeatherParser.parse_forecast(forecast)
            WeatherDisplay.display_forecast(parsed_forecast)

    def show_help(self):
        print("\nCommands:")
        print("  help       - Show commands")
        print("  quit       - Exit app")
        print("  favorites  - Show saved cities")

    def show_favorites(self):
        if FAVORITES_FILE.exists():
            with open(FAVORITES_FILE, "r") as f:
                favorites = json.load(f)
                print("\nFavorite Cities:")
                for city in favorites:
                    print(f"- {city}")
        else:
            print("No favorites saved.")


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
