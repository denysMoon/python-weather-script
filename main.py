import requests
import cowsay
from dotenv import load_dotenv
import os


def get_weather(city):
    load_dotenv()

    api_key = os.getenv("OPENWEATHERMAP_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        cloudiness = data["clouds"]["all"]

        if "rain" in data:
            rainfall = data["rain"].get("1h", 0)
        else:
            rainfall = 0

        print(f"Weather in {city}:")
        print(f"  - Temperature: {temperature} °C")
        print(f"  - Feels like: {feels_like} °C")
        print(f"  - Cloudiness: {cloudiness}%")
        print(f"  - Rainfall (last hour): {rainfall} mm")
        print(f"  - Overall: {weather} ({description})")
    else:
        cowsay.milk(f"Failed to retrieve weather data for {city}.")


while True:
    city = input("Enter the city name (or 'quit' to exit): ")

    if city.lower() == "quit":
        break

    get_weather(city)
