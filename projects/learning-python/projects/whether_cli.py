# ### 11. Weather CLI
# Fetch and display current weather for a city.
# - **Requirements:** use a free API (e.g. Open-Meteo — no key needed, or
#   OpenWeatherMap with a key in an env var); take a city name; print temp +
#   conditions; handle network errors and unknown cities gracefully.
# - **You'll learn:** `requests`/`httpx`, JSON responses, env vars for secrets, error handling.
# - **Stretch:** cache results for 10 minutes; 3-day forecast.

import requests
import sys

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Heavy rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}

def get_city_coordinates(city):
    try:
        response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("results"):
            return None

        result = data["results"][0]

        return {
            "name": result["name"],
            "country": result.get("country", ""),
            "latitude": result["latitude"],
            "longitude": result["longitude"],
        }

    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching city data: {e}")
        return None


def get_weather(lat, lon):
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,weather_code"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()["current"]

    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching weather: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python weather_cli.py <city>")
        return

    city = " ".join(sys.argv[1:])

    print(f"\nFetching location for '{city}'...\n")

    location = get_city_coordinates(city)

    if not location:
        print(f"Unknown city: '{city}'")
        return

    print(
        f"Found: {location['name']}"
        f"{', ' + location['country'] if location['country'] else ''}"
    )

    print("\nFetching weather...\n")

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    if not weather:
        return

    temperature = weather["temperature_2m"]
    weather_code = weather["weather_code"]

    condition = WEATHER_CODES.get(
        weather_code,
        f"Unknown ({weather_code})"
    )

    print("Result: \n")
    print(f" - Temperature: {temperature}°C")
    print(f" - Condition: {condition}")
    print(f"")


main()


