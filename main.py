import agentops
from crewai import Crew
from langchain_community.llms import Ollama

from dotenv import load_dotenv
import os

from tool.custom_tool import validate_city
from agents import MorningAgent
from tasks import MorningTask

load_dotenv()

AGENTOPS_API_KEY = os.getenv('AGENTOPS_API_KEY')

agentops.init(AGENTOPS_API_KEY)
ollama_model = Ollama(model="openhermes")

BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if OPENWEATHER_API_KEY is None:
    raise ValueError("OPENWEATHER_API_KEY not found in environment variables.")


def run():
    print("Hi, I am your morning agent. I can help you to gather top headline news and "
          "weather of the place that you are staying at. So, start by telling me where your location is at.")
    city = input("Enter Your City: ")
    is_city = validate_city(city)
    if is_city is False:
        print("We are not able to find your city to check the weather for.")
        return

    agents = MorningAgent()
    tasks = MorningTask()

    # Create Agents
    weather_seeker_agent = agents.weather_seeker(user_city=city)
    collect_news_agent = agents.news_collector(user_city=city)
    morning_chat_agent = agents.morning_advisor()

    # Create Tasks
    research_weather = tasks.research_weather(weather_seeker_agent)
    collect_news = tasks.collect_news(collect_news_agent)
    writing_task = tasks.writing_task(morning_chat_agent)

    # Create crew responsible for MorningAgent
    morning_crew = Crew(
        agents=[
            weather_seeker_agent,
            collect_news_agent,
            morning_chat_agent
        ],
        tasks=[
            research_weather,
            collect_news,
            writing_task,
        ],
        verbose=True
    )

    morning_speech = morning_crew.kickoff()

    agentops.end_session('Success')

    print("Hello sir,")
    print(morning_speech)


if __name__ == "__main__":
    run()
