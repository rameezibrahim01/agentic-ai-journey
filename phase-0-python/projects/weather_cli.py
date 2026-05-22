import requests
import os
from dotenv import load_dotenv
import truststore
truststore.inject_into_ssl()
from pydantic import BaseModel
import json
from datetime import datetime


class Wind(BaseModel):
    speed:float

class Sys(BaseModel):
    country: str

class Main(BaseModel):
    temp: float
    feels_like: float
    humidity: int

class Weather(BaseModel):
    description: str

class WeatherResponse(BaseModel):
    sys: Sys
    wind: Wind
    main: Main
    weather:list[Weather]
    name:str



load_dotenv()

key = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city name: ")
 
try:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric", timeout = 5)
    data = response.json()
    weather = WeatherResponse(**data)
    print(f"Response:\nCity: {weather.name}\nCountry: {weather.sys.country}\nWind Speed: {weather.wind.speed}\nTemp: {weather.main.temp}\nConditions: {weather.weather[0].description}")
    
    try:
        saved_data = []
        with open("phase-0-python/week-2/output-files/history.json", "r") as f:
            saved_data = json.load(f)
    except FileNotFoundError:
        saved_data = []
        print("File not found")

    with open("phase-0-python/week-2/output-files/history.json", "w") as f:
        parsed_data = {"timestamp": str(datetime.now()), "city": weather.name, "temp": weather.main.temp}
        saved_data.append(parsed_data)
        json.dump(saved_data, f, indent = 2)

except requests.Timeout:
    print(f"Request timed out")
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
