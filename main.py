import os
from decouple import config
import openai

openai.api_key = config("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are an intelligent assistance"}
]

while True:
    try:
        user_query = input("User : ")
        if user_query:
            messages.append(
                {"role": "user", "content": user_query},
            )
            chat_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=messages
            )

        reply = chat_response.choices[0].message.content
        print(f"ChatGPT Response => {reply}")
        messages.append(
            {"role": "assistant", "content": reply}
        )
    except Exception as err:
        print("An error occurred with error message => ", err)
        exit('AI is stopping now...')