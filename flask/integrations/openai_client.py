from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIClient:
    def __init__(self):
        apiKey = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=apiKey)

    def summarize(self, messages, model="gpt-3.5-turbo", temperature=0.7):

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response
