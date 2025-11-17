
import openai

openai.api_key = "your-api-key"

def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": message}]
    )
    return response['choices'][0]['message']['content']

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye"]:
        print("Bot: Goodbye!")
        break
    reply = ask_gpt(user_input)
    print(f"Bot: {reply}")