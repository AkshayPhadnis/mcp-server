# llm_handler.py

import os
import openai
from dotenv import load_dotenv

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# def handle_llm(user_message: str) -> str:
#     prompt = f"User asked: {user_message}"
#     try:
#         client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )

#         llm_response = response.choices[0].message.content


#         return llm_response#response['choices'][0]['message']['content'].strip()

#     except Exception as e:
#         return f"Error from LLM: {e}"


def handle_llm(message, context):
    # You can now use both inputs as needed
    return f"User asked: {message}. Response is: {context}"
