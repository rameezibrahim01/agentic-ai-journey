
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import httpx
import asyncio
import time

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

async def fetch_weather(city: str) -> WeatherResponse | None:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
        weather_json = response.json()
        weather_response = WeatherResponse(**weather_json)
        return weather_response


async def fetch_five_cities_weather():
    try:
        start = time.time()

        weather_list = await asyncio.gather(fetch_weather("delhi"), fetch_weather("new york"), fetch_weather("dubai"), fetch_weather("mumbai"), fetch_weather("abu dhabi"))
        

        print(f"{'City':<12} {'Temp':<12} {'Humidity':<12}" )
        for weather in weather_list:
            print(f"{weather.name:<12} {weather.main.temp:<12} {weather.main.humidity:<12}" )
        

        elapsed = time.time() - start
        estimated_sequential = elapsed * 5
        print(f"\nFetched in {elapsed:.2f}s (sequential would take ~{estimated_sequential:.1f}s)")

    except httpx.HTTPError as e:
        print(f"HTTP Error: {e}")
    except httpx.RequestError as e:
        print(f"Requests Error: {e}")


asyncio.run(fetch_five_cities_weather())