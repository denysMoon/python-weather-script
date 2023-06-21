import requests


def get_weather(city):
    # Temporary API key for testing
    api_key = "4744245dfa7abc19a9387260236687f2"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send the API request
    response = requests.get(url)
    data = response.json()

    # Extract and print the weather information
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
        print(f"Failed to retrieve weather data for {city}.")


# User input for city
city = input("Enter the city name: ")

# Get the weather information for the city
get_weather(city)
