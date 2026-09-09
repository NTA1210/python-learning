import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.chat_models import init_chat_model

load_dotenv()

@tool('get_weather', description='Return weather information for a given city.', return_direct=False)
def get_weather(city:str):
    headers = {
    "User-Agent": "Mozilla/5.0 (LangChain Bot)"
}
    response = requests.get(f'http://wttr.in/{city}?format=1', timeout=10,headers=headers)
    print(response ,end="\n")
    return response 


model = init_chat_model('gpt-3.5-turbo',temperature=0.5, timeout = 10, verbose=True, max_tokens=1000)

agent = create_agent(
  model = model,
  tools=[get_weather],
  system_prompt='You are a helpful assistant that answers questions about the weather.',
)

response = agent.invoke({
  'messages': [
    {
      'role': 'user',
      'content': 'What is the weather in New York?'
    }
  ]
})

print(response['messages'][-1]['content'])