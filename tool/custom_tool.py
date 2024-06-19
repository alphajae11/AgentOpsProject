import agentops
from agentops import record, ToolEvent
from crewai_tools import tool
from geopy.geocoders import Nominatim
from langchain_community.llms import Ollama

from dotenv import load_dotenv
import json
import os
import pycountry
import requests

load_dotenv()

AGENTOPS_API_KEY = os.getenv('AGENTOPS_API_KEY')
agentops.init(AGENTOPS_API_KEY)
ollama_model = Ollama(model="openhermes")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

NEWS_URL = "https://newsapi.org/v2/top-headlines?"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def validate_city(city):
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return city
    else:
        return False


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


@tool("Weather Analyst Tool")
def get_weather(city: str) -> str:
    """Get the details of weather at the city by querying the Open Weather Map API"""
    url = BASE_URL + "q=" + city + "&APPID=" + OPENWEATHER_API_KEY
    tool_event = ToolEvent(name='get_weather', params={'url': url})
    response = requests.get(url)
    tool_event.returns = response
    record(tool_event)

    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data["main"]["temp"]
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        feels_like_kelvin = data["main"]["feels_like"]
        feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        summary = {
            "temperature": temp_celsius,
            "feels_like": feels_like_celsius,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "general_weather": description
        }
        return json.dumps(summary, indent=2)
    else:
        return json.dumps({"error": "API request failed", "status_code": response.status_code}, indent=2)


def get_country_code(city_name):
    # Initialize geolocator
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Get location from city name
    location = geolocator.geocode(city_name)

    if not location:
        return None

    # Get country name from location
    country_name = location.address.split(',')[-1].strip()

    # Get country code from country name
    country = pycountry.countries.get(name=country_name)

    if not country:
        return None

    return country.alpha_2


@tool("Collect News")
def get_news(city: str) -> str:
    """Collecting top headlines in the city by querying the News API"""
    country_code = get_country_code(city)
    print(country_code)
    main_url = NEWS_URL + "country=" + country_code + "&apiKey=" + NEWS_API_KEY

    # Get all news in json format from News API
    response = requests.get(main_url)

    if response.status_code == 200:
        open_news_page = response.json()

        # Get all articles in a string article
        article = open_news_page["articles"]

        # Gather news to results first
        results = []

        for ar in article:
            results.append(ar["title"])

        summary = ""

        for i in range(len(results)):
            n = i + 1
            summary = summary + str(n) + results[i]

        return summary
    else:
        return json.dumps({"error": "API request failed", "status_code": response.status_code}, indent=2)


