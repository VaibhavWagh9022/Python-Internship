from weather_app.weather_parser import WeatherParser

def test_temperature_conversion():
    assert WeatherParser.to_fahrenheit(0) == 32.0
