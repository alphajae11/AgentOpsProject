## What I enjoyed from this project?
Despite having a few difficulties from this project, I deeply enjoyed doing this project. From this project, I wanted to explore a few interesting ideas that 
can be useful for me in real life. Remembering how my dad like to play around with Apple Siri in the morning, I wanted to build my own little version of Siri - Morning Agent.
For this simple project, I wanted my agent to gather some top headline news and the weather in the morning. The first output for the first successful attempt of building AI agent was:

```Based on the current weather in Singapore, here is some detailed advice for going outdoors:```

```1. **Clothing**: Given the temperature of 28.9°C but feeling like 34.25°C due to high humidity, it's best to wear light, breathable fabrics such as cotton or linen. Opt for short sleeves or sleeveless tops and shorts or skirts to stay cool.```

```2. **Rain Gear**: Since there is light rain, carrying an umbrella or a lightweight raincoat is advisable. Waterproof footwear can also be a good idea to keep your feet dry.```

```3. **Hydration**: With the humidity at 79%, it's easy to become dehydrated. Make sure to drink plenty of water throughout the day. Carry a reusable water bottle with you.```

```4. **Sun Protection**: Even though it's raining, UV rays can still penetrate through the clouds. Apply a broad-spectrum sunscreen with at least SPF 30, wear sunglasses, and consider a hat to protect your face and eyes.```

```5. **Footwear**: Comfortable, waterproof shoes are recommended due to the light rain. Avoid wearing flip-flops or sandals that can become slippery when wet.```

```6. **Accessories**: A small, portable fan can be useful to combat the heat and humidity. Also, consider carrying a small towel or handkerchief to wipe off sweat.```

```7. **Watch Out For**: Be cautious of slippery surfaces due to the rain. Walk carefully to avoid any accidents. Also, keep an eye on weather updates in case the rain intensifies.```

```By following these tips, you can stay comfortable and safe while navigating the weather in Singapore. Enjoy your day!```

With the integration of AgentOps SDK to analyze the process in which this output was created by my AI agent, I managed to refine my current AI agent in a way I want to respond. Using AgentOps also allow me to compare performance between the OpenAI and Ollama models (in terms of speed). 

The best part of this project was when I finally managed to make it come up with a 2 paragraph output (with clear details about weather and top headline news) based on the input - the city that user is at:

```Input: Singapore```

```Good morning! As you prepare to head out today, please be aware that the weather forecast indicates short, thundery showers in the late morning and afternoon for most days for the rest of June. It would be wise to carry an umbrella and wear waterproof shoes to stay dry. Additionally, consider wearing light, breathable clothing to stay comfortable in the humid conditions that often accompany such weather. Keep an eye on the sky and be prepared to seek shelter if you notice dark clouds forming.```

```In today's headlines, there are several noteworthy stories. Satellite imagery has captured a close-up photo of a giant piece of space junk, highlighting the growing concern over debris in Earth's orbit. In sports, the Premier League fixtures have been announced, with Chelsea set to face Manchester City in the opening term. On a more local note, Singapore has reclaimed the top spot in the world competitiveness ranking after three years, a testament to the nation's robust economic policies and business environment. Lastly, authorities have issued a bird flu advisory, urging the public to avoid touching or feeding wild birds to prevent the spread of the virus. Stay informed and have a great day!```

I believe that more improvements can be made to this AI agents via conducting further extension to this project.

## What I found difficult from this project?

### 1. Building AI Agent to specifically to what I want it to be like was one of the difficulties that I faced in this project.
In many occasions, I had to rewrite and change the words used to describe the role, goal and backstory within the agent as well as the description and expected output within the task - 
to ensure that the Agent is processing in a way that I want it to process when carrying out the function.
With the help of analysis from AgentOps SDK, this was slightly easier to work with.
However, the analysis was only so when OpenAI Model was used (No Analysis was shown when Ollama model was used)

### 2. Lack of Analysis for Ollama Model
When I used Ollama model to build my AI agent and integrate with AgentOps SDK, there was not much analysis of how my AI agent is being processed.
Unlike OpenAI model, AgentOps did not show how Ollama model was processing when I am running the AI agent.

### 3. Trying to debug and see why there is error in the agent 
There are quite a few times when my model just failed to run due to some bugs or errors within the source code. 
Although AgentOps.AI showed the error messaged raised, it was still very difficult to see where I had possibly made some mistake in my source code. 
Relatively long time was spent to debug these errors or even fix the source code to build the agent in a way that I wanted it to be.

### My Thoughts about Possible Feature Enhancements for AgentOps.AI
Based on some of the difficulties I faced during this project. I personally think that below are some possible ways to make further improvements to this AgentOps.AI 
if I am given an opportunity.

- Addition of feature that analyzes the process of local models such as Ollama
- Addition of feature that gives some possible analyzed reasons for the error or failure of the AI Agents
- Improvement in the @trackagent decorator feature: 

The reason for the third point was because @trackagent decorator did not work as I thought it would be. 
Although the AgentOps showed the name of the different agents that I had made, it did not explicitly show event data for each agents.

## What values I found from this project?
Below are some values that I found from this project:

1. Deeper understanding of how AI agents operate and are built
2. Experimentation with different AI models and determining difference in performance of different AI model (OpenAI and Ollama models)
3. Understanding the potentially powerful and practical application of AI agents
4. Enhancing efficiency and effectiveness of AI agents to optimize its performance
5. Importance of internal tools such as AgentOps SDK that helps to analyse how the AI agent is being processed