# bot/ai.py
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_gpt(message: str) -> str:
    # Validate input
    if not message or not message.strip():
        return "I need a message to respond to. Please send me something to chat about!"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful WhatsApp assistant"},
                {"role": "user", "content": message.strip()},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "Sorry, I'm having trouble processing your message right now. Please try again later."
