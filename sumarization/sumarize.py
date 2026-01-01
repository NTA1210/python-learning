import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken

MAX_TOKENS = 900
MAX_PROMPT_TOKENS = 700


def read_text_file(file_path):
    f = open(file_path)
    return f.read()

def chunk_text(text, max_tokens = MAX_PROMPT_TOKENS):
    tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = tokenizer.encode(text)
    chunks=[]
    for i in range(0, len(tokens),max_tokens):
        chunk = tokens[i:i+max_tokens]
        chunks.append(tokenizer.decode(chunk))
    return chunks

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
            messages =  context,
            temperature = 0.7
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
    print('Total tokens: ',len(tiktoken.encoding_for_model("gpt-3.5-turbo").encode(text)))

    chunks = chunk_text(text)

    if len(chunks) == 1:
        summarize_text = summarize(client, text)
        print("\n =======================\n")
        print(summarize_text)
    else:
        print("\n Have to chunk the text \n")
        print("CHUNKS: ", len(chunks),"\n")
        chunk_summaries = []
        for chunk in chunks:
            summarize_text = summarize(client, chunk)
            if summarize_text is not None:
                chunk_summaries.append(summarize_text)

        combined_summaries = " ".join(chunk_summaries)
        final_summary = summarize(client, combined_summaries)
        print("\n =======================\n")
        print(final_summary)