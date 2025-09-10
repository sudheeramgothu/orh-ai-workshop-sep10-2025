import requests

# Simple geocoding service from Open‑Meteo (free, no key) to get lat/lon for a city
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city: str):
    resp = requests.get(GEOCODE_URL, params={"name": city, "count": 1})
    resp.raise_for_status()
    data = resp.json()
    if not data.get("results"):
        raise ValueError(f"Could not find coordinates for city '{city}'")
    r0 = data["results"][0]
    return float(r0["latitude"]), float(r0["longitude"]), r0.get("country", "Unknown")

def get_weather_for_city(city: str):
    lat, lon, country = geocode_city(city)
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,wind_speed_10m",
        "current_weather": True
    }
    resp = requests.get(FORECAST_URL, params=params)
    resp.raise_for_status()
    data = resp.json()
    # Return a small, friendly summary
    summary = {
        "location": {"city": city, "country": country, "lat": lat, "lon": lon},
        "current": data.get("current_weather", {}),
        "sample_hourly": {
            "temperature_2m": data.get("hourly", {}).get("temperature_2m", [])[:6],
            "precipitation": data.get("hourly", {}).get("precipitation", [])[:6],
            "wind_speed_10m": data.get("hourly", {}).get("wind_speed_10m", [])[:6],
        }
    }
    return summary
