from crewai import Task


class MorningTask:
    def research_weather(self, agent):
        return Task(
            description="Get the summary of weather (temperature, feels_like, wind_speed, humidity, general_weather) at the city",
            expected_output='A summary of weather (temperature, feels_like, wind_speed, humidity, general_weather) at the city',
            # tools=[get_weather],
            agent=agent,
        )

    def collect_news(self, agent):
        return Task(
            description="Collect 10 top headline news at the city",
            expected_output='list of 10 top headline news at the city',
            agent=agent,
        )

    def writing_task(self, agent):
        return Task(
            description="""Write 2 paragraphs - one for user about some advice when going outdoors based on the weather data 
            and another for top headline news based on the top headline news data""",
            expected_output="""2 paragraphs - one for user about some advice when going outdoors based on the weather data 
            and another for top headline news based on the top headline news data""",
            agent=agent,
        )
