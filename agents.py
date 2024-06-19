import agentops
from agentops import track_agent
from crewai import Agent
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

from tool.custom_tool import get_weather, get_news

load_dotenv()
AGENTOPS_API_KEY = os.getenv('AGENTOPS_API_KEY')
agentops.init(AGENTOPS_API_KEY)

# OpenAI key if being used
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class MorningAgent:
    def __init__(self):
        # Ollama Model
        # self.llm = Ollama(model="openhermes")

        # OpenAI Model
        self.llm = ChatOpenAI(
                model="gpt-4o",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            )

    @track_agent(name="weather_seeker")
    def weather_seeker(self, user_city):
        return Agent(
            role="weather analyst",
            goal="Get the summary of weather (temperature, feels_like, wind_speed, humidity, general_weather) at"
                 + user_city,
            verbose=True,
            backstory="As a weather seeker, you are able to get the " +
                      "temperature, feels_like, wind_speed, humidity, general_weather of the" + user_city + ".",
            llm=self.llm,
            tools=[get_weather],
            allow_delegation=False
        )

    @track_agent(name="news_collector")
    def news_collector(self, user_city):
        return Agent(
            role="news collector",
            goal="Collect 10 top headline news at the" + user_city,
            verbose=True,
            backstory="As a news collector, you are able to collect top 10 news at the" + user_city + ".",
            llm=self.llm,
            tools=[get_news],
            allow_delegation=False
        )

    @track_agent(name="morning_advisor")
    def morning_advisor(self):
        return Agent(
            role="weather advisor",
            goal="""Write 2 paragraph - one for user about some advice when going outdoors based on the weather data 
            and another for top headline news based on the top headline news data""",
            verbose=True,
            backstory="""
            You are a house butler who can compose some advice for house owner who is going outdoors 
            based on the weather and collect top headline news based on the top headline news.
            With a talent of good communication, you are supposed to write 2 short paragraphs for your owner.
            In the first paragraph, with a talent of analysing the weather, you can advise the user on 
            what user should wear or watch out for when he or she goes outside for work or etc.
            In the second paragraph, with good general knowledge, you can tell some top headline news to share
            """,
            llm=self.llm,
            allow_delegation=False
        )
