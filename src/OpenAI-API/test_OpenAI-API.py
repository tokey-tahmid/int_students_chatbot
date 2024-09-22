'''
from openai import OpenAI

client = OpenAI(api_key="#")


messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
'''

import openai
import time  # Ensure time is imported for handling rate limits

client = openai.OpenAI(api_key="#")

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    user_input = input("Enter your message (or type 'quit()' to exit): ")
    if user_input.lower() == "quit()":
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response.choices[0].message.content  # Access content directly
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")
    except openai.RateLimitError:  # Correctly reference RateLimitError
        print("Rate limit exceeded, please try again later.")
        time.sleep(60)  # wait for a minute before trying again
    except openai.OpenAIError as e:  # Correctly reference OpenAIError
        print(f"An error occurred: {e}")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
