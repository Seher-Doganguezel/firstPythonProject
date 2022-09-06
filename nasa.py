import requests
import json

api_key = "d545f39634fec99e97a5516c0f9ad8f5"
city = input("Gibt eine Stadt ein.")

url = f"https://api.openweathermap.org/data/2.5/weather?lat={city}&appid={api_key}"

dataW = requests.get(url).json()

temperatur = dataW["main"]["speed"]

print(f"In {city} beträgt das Wetter {temperatur}")
