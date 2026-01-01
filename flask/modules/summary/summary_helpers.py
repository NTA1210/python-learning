import tiktoken

MAX_TOKENS = 1000
MAX_PROMPT_TOKENS = 800

def count_tokens(text: str, model="gpt-3.5-turbo"):
    return len(tiktoken.encoding_for_model(model).encode(text))


def chunk_text(text: str, max_tokens=MAX_PROMPT_TOKENS, model="gpt-3.5-turbo"):
    tokenizer = tiktoken.encoding_for_model(model)
    tokens = tokenizer.encode(text)

    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunks.append(tokenizer.decode(tokens[i:i + max_tokens]))

    return chunks
