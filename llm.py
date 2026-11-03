
from google import genai
from google.genai import types

from config import API_KEY, MODEL_NAME
from tools import recommend_laptops

client = genai.Client(api_key=API_KEY)

SYSTEM_INSTRUCTION = """
You are an AI Laptop Decision Assistant for the Indian market.

Your job is to help users choose laptops.

RULES:

1. Understand the user's requirements.

2. If important requirements are unclear,
ask a clarifying question.

3. When enough requirements are available,
call the recommend_laptops Python tool.

4. Never calculate laptop scores yourself.

5. Never invent laptop specifications,
prices or Internal Dataset Performance Scores.

6. If the Python tool returns no results,
explain that no laptop matches the requirements.

7. You may explain the closest alternatives,
but clearly state when they do not satisfy
the original requirements.

8. Separate factual specifications and scores
from your AI-generated recommendation.

9. Keep responses simple and helpful.

10. Never claim that illustrative dataset prices
are verified live market prices.
"""


def create_chat():

    chat = client.chats.create(
        model=MODEL_NAME,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            tools=[recommend_laptops],
            temperature=0.2
        )
    )

    return chat


def send_message(chat, message):

    response = chat.send_message(message)

    return response.text
