import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken

MAX_TOKENS = 2000


def read_text_file(file_path):
    f = open(file_path)
    return f.read()


def summarize(client, text):
    context = [
       { 'role': 'system',
        'content':'You are a helpful assistant that summarizes text. Please summarize the following text in a concise and clear way.'
        },
        {
            'role':'user',
            'content':text
        }
    ]
    try:
        response = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages =  context
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    print("TOTAL TOKENS: ",response.usage.total_tokens)

    return response.choices[0].message.content


if __name__ == "__main__":

    load_dotenv()

    apiKey = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=apiKey)

    text = read_text_file('data.txt')
    print('Length: ',len(text))

    summarize_text = summarize(client, text)
    print("\n =======================\n")
    print(summarize_text)
