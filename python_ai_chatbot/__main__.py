import python_ai_chatbot

def main():
    messages = python_ai_chatbot.json_to_messages("python_ai_chatbot/test_json_data.json")
    vectorized_messages = python_ai_chatbot.vectorize_messages(messages)
    print(vectorized_messages)

if __name__ == "__main__":
    main()
