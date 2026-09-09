import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool,ToolRuntime
from langchain.chat_models import init_chat_model
from dataclasses import dataclass
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy
from langchain_core.output_parsers import JsonOutputParser  

from typing import Union



load_dotenv()

@dataclass
class Context:
    user_id: str
  
@dataclass
class ResponseFormat:
    response:str
    temperature_celsius:float| None = None
    temperature_fahrenheit:float| None = None
    humidity:float| None = None

@dataclass
class TextResponseFormat:
    response:str

@tool('get_weather', description='Return weather information for a given city.')
def get_weather(city: str):
    headers = {"User-Agent": "Mozilla/5.0 (LangChain Bot)"}
    r = requests.get(f'http://wttr.in/{city}?format=j1', headers=headers)
    data = r.json()

    current = data["current_condition"][0]
    return {
        "response": f"Weather in {city}",
        "temperature_celsius": float(current["temp_C"]),
        "temperature_fahrenheit": float(current["temp_F"]),
        "humidity": float(current["humidity"]),
    }


@tool('locate_user', description="Look up a user's city based on the context", return_direct=False)
def locate_user(runtime:ToolRuntime[Context]):
    match runtime.context.user_id:
        case "1":
            return "New York"
        case "2":
            return "London"
        case "3":
            return "Tokyo"
        case _:
            return "San Francisco"


model = init_chat_model('gpt-3.5-turbo',temperature=0.8, timeout = 10, max_tokens=1000)

check_pointer = InMemorySaver()

chain = model.pipe(JsonOutputParser())

agent = create_agent(
  model = chain,
  tools=[get_weather,locate_user],
  system_prompt='You are a helpful assistant that answers questions about the weather.',
  context_schema=Context,
#   response_format=ToolStrategy(Union[ResponseFormat,TextResponseFormat]),
  checkpointer=check_pointer
)

config = {"configurable": {"thread_id": "1"}}


response = agent.invoke({
  'messages': [
    {
      'role': 'user',
      'content': 'What is the weather?'
    }
  ]
},config=config, context=Context(user_id="1"))

print(response)
# print(response)
# print(response)

# response = agent.invoke({
#   'messages': [
#     {
#       'role': 'user',
#       'content': 'And is this usual?'
#     }
#   ]
# },config=config, context=Context(user_id="1"))

# print(response)
# # print(response)
