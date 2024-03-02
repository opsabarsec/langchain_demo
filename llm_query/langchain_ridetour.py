"""Bike tour advice module"""
# import libraries
from  llm_query import langchain_example
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI

# This line brings all environment variables from .env
# into os.environ
load_dotenv()
# AGENT that will bring weather info
llm = OpenAI(temperature=0)
tools = load_tools(["openweathermap-api"], llm)

agent_chain = initialize_agent(tools=tools, 
                            llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                            verbose=False)
# the advisor is the LLM imported from langchain_example module
advisor = langchain_example.Pred()
class GetWeather:
    """Get the weather from OpenweatherMap"""
    global agent_chain
    # the agent is imported into this class
    def __init__(self):
        self.agent_chain = agent_chain
    # this class function returns the current weather for the city inputed
    def answer(self, city) -> str:
        return agent_chain.run(f"What's the weather like in {city}?")

class RideAdvice(GetWeather):
    """Get the bike tour advice from LLM"""
    global advisor
    # I initialize the module and define the additional question to pose to the LLM
    def __init__(self):
        GetWeather.__init__(self)
        self.add_sentence = " Is it good weather for cycling? And what are the best places to visit there?"
    # I combine the output of OpenWeatherAPI to the question above     
    def tour_advice(self, city):
        weather_prompt = str(self.answer(city)+self.add_sentence)
        # I feed the combined sentence as a question to the LLM
        tourist_advice = advisor.answer(weather_prompt)  
        return tourist_advice
