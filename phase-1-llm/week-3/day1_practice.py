import asyncio
import httpx
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import requests

print("•	Write async function fetch_fact() that calls catfact.ninja. Fetch 5 facts concurrently with asyncio.gather(). Print all 5 facts.")

async def fetch_fact():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://catfact.ninja/fact")
        return response.json()["fact"]


async def fetch_five_facts():
    facts = await asyncio.gather(fetch_fact(), fetch_fact(), fetch_fact(), fetch_fact(), fetch_fact())
    for index, fact in enumerate(facts, 1):
        print(f"{index}: {fact}")

asyncio.run(fetch_five_facts())



print("•	Write async function fetch_weather(city) that calls OpenWeatherMap (from Phase 0). Fetch 3 cities simultaneously. Print all results.")

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


async def fetch_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
        data = response.json()
        weather = WeatherResponse(**data)
        # print(f"Response:\nCity: {weather.name}\nCountry: {weather.sys.country}\nWind Speed: {weather.wind.speed}\nTemp: {weather.main.temp}\nConditions: {weather.weather[0].description}")
        return weather

async def fetch_three_cities_weather():
    weathers = await asyncio.gather(fetch_weather("dubai"), fetch_weather("abu dhabi"), fetch_weather("delhi"))
    for index, weather in enumerate(weathers, 1):
        print(f"{index}. {weather.name} : {weather.main.temp}")

asyncio.run(fetch_three_cities_weather())


print("•	Time comparison: write the same task (fetch 5 cat facts) synchronously using requests AND async using httpx. Print elapsed time for each. How much faster is async?")
import truststore
truststore.inject_into_ssl()
import time

def get_cat_facts_requests():
    response = requests.get("https://catfact.ninja/fact", timeout = 5)
    return response.json()["fact"]

# Time the sync version
start = time.time()
asyncio.run(fetch_five_facts())
sync_time = time.time() - start
print(f"\nSync time: {sync_time:.2f}s")

# Sync timing
start = time.time()
for i in range(5):
    print(get_cat_facts_requests())
sync_time = time.time() - start
print(f"\nSync time: {sync_time:.2f}s")

# Async timing
start = time.time()
asyncio.run(fetch_five_facts())
async_time = time.time() - start
print(f"\nAsync time: {async_time:.2f}s")

print(f"\nAsync was {sync_time / async_time:.1f}x faster")
