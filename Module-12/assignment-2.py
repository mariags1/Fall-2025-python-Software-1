# make HTTP requests
import requests

# Stores your OpenWeather API key as a variable
api_key = "2af40317bfd5ccb9fde188cff9ec7396"

# We will add parameters like city name and API key to this URL to get weather data
base_url = "https://api.openweathermap.org/data/2.5/weather"

keyword = input("Enter municipality name: ")

full_url = f"{base_url}?q={keyword}&appid={api_key}&units=metric"

try: # allows error handling
    response = requests.get(full_url) # Sends a GET request to the API using the URL

    data = response.json() # Converts the API response from JSON format to a Python dictionary

    # weather description from the dictionary
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather: {weather_description}")
    print(f"Temperature: {temperature} Celsius")

# error handling
except requests.exceptions.RequestException as e:
    print(f"HTTp Error: {e}")
    print("Could not retrieve weather data. Please check the municipality name and your API key")
