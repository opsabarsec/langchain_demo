"""Bike tour advice module"""
from  llm_query import langchain_example
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI
# This line brings all environment variables from .env
# into os.environ

load_dotenv()

llm = OpenAI(temperature=0)
tools = load_tools(["openweathermap-api"], llm)

agent_chain = initialize_agent(tools=tools, llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)
advisor = langchain_example.Pred()
class GetWeather:
    """Get the weather from LLM"""
    global agent_chain

    def __init__(self):
        self.agent_chain = agent_chain

    def answer(self, city) -> str:
        return agent_chain.run(f"What's the weather like in {city}?")

class RideAdvice(GetWeather):
    """Get the bike tour advice from LLM"""
    global advisor
    def __init__(self):
        GetWeather.__init__(self)
        self.add_sentence = " Is it good weather for cycling?. And what are the best place to visit there?"
        
    def tour_advice(self, city):
        weather_prompt = str(self.answer(city)+self.add_sentence)
        tourist_advice = advisor.answer(weather_prompt)  
        return tourist_advice
