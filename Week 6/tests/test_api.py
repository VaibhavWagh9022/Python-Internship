from weather_app.weather_api import WeatherAPI

def test_api_creation():
    api = WeatherAPI()
    assert api is not None
