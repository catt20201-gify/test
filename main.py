import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Riyadh"

def get_weather():
    if not API_KEY:
        raise ValueError("API_KEY is missing!")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])

get_weather()
