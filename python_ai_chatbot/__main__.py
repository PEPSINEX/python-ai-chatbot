import os
from dotenv import load_dotenv
import python_ai_chatbot

def main():
    load_dotenv()
    SAMPLE_KEY = os.getenv("SAMPLE_KEY")

    messages = python_ai_chatbot.json_to_messages("python_ai_chatbot/test_json_data.json")

    print(messages)

if __name__ == "__main__":
    main()
