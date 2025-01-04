import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def vectorize_message(message):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=message
    )
    return response.data[0].embedding

def vectorize_messages(messages):
    for msg in messages:    
        msg["vector"] = vectorize_message(msg["text"])

    return msg
