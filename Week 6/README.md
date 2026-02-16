# 🌤 Weather Dashboard Application (Week 6 Final Project)

A menu-driven Weather Dashboard Application built using External Libraries, API integration, JSON processing, and modular architecture in Python.
This project allows users to fetch real-time weather data, view 5-day forecasts, and manage weather queries using persistent caching and secure API handling.

## 📌 Project Overview

Fetching weather information manually from websites can be time-consuming and inefficient.
This project provides a command-line application that allows users to:

Search weather for any city worldwide

View current weather conditions

View 5-day forecast

Display humidity, pressure, and wind speed

Cache API responses to reduce unnecessary API calls

Securely store API keys using environment variables

Handle invalid cities and network errors

The project demonstrates real-world implementation of External API Integration concepts learned in Week 6.

## 🎯 Objectives

Understand and integrate external APIs

Work with HTTP requests using requests

Parse and process complex JSON data

Implement environment variable management

Design modular project architecture

Implement caching mechanism

Practice debugging and API error handling

Build a real-world Python CLI application

## 🛠️ Technologies Used

Language: Python 3.x

API Service: WeatherAPI.com

File Format: JSON

Concepts:

External API Integration

HTTP Requests

JSON Parsing

Environment Variables

Caching

Exception Handling

Modular Programming

Unit Testing

## 📂 Project Structure
```
week6-weather-dashboard/
│
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│
├── data/
│   ├── cache/
│   └── favorites.json
│
└── tests/
    ├── test_api.py
    ├── test_parser.py
    └── test_display.py
```

## ⚙️ Features Implemented
🌍 Current Weather

Search weather by city name

Display:

City & Country

Temperature

Feels like temperature

Weather condition

Humidity

Wind speed

Pressure

Last updated time

📅 5-Day Forecast

Display daily forecast including:

Date

Maximum temperature

Minimum temperature

Weather condition

## 📊 Application Workflow

User enters city
↓
API request sent to WeatherAPI
↓
JSON response received
↓
Data parsed into structured format
↓
Weather displayed in formatted CLI output
## ▶️ How to Run the Project
## Step 1: Navigate to Project Folder
```bash
cd week6-weather-dashboard
```
## Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
Step 3: Add API Key
Create .env file in root directory:
API_KEY=your_api_key_here
Step 4: Run the Application
```bash
python -m weather_app.main
```
🧭 Sample Menu
Enter city (or help/quit/favorites):

> pune

📌 Sample Output
🌤 WEATHER DASHBOARD
==============================
📍 Pune, India
🕐 Updated: 2026-02-16 00:30

Temperature: 22.0°C
Feels Like: 22.0°C
Condition: Clear
Humidity: 37%
Wind Speed: 8.6 kph
Pressure: 1014.0 mb

5-Day Forecast
------------------------------
2026-02-16 | Max: 29.0°C | Min: 18.0°C | Sunny
