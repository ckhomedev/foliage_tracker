import requests
import json

open_weather_api = "94416a6a67de9bb9240dae1cd97a1e6a"
# weather_url = "https://api.openweathermap.org/data/2.5/weather?"
weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=41.3542656&lon=-71.966462&appid=94416a6a67de9bb9240dae1cd97a1e6a"
print(weather_url)
# mystic lat and lon
params = {
    "lat": 41.3542656,
    "lon": -71.966462,
    "appid": open_weather_api,
    "units": "imperial"}

data = requests.get(weather_url, params)
weather = data.json()
print(weather)
print(weather['coord'])
print(weather['main'])
print(weather['dt'])
print(weather['weather'][0]['description'])
