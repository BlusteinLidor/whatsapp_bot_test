from fastapi import FastAPI, Request
import uvicorn
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

app = FastAPI()
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
SYSTEM_USER_ACCESS_TOKEN = os.getenv("SYSTEM_USER_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


# 1. Webhook verification (GET)
@app.get("/webhook")
async def verify(request: Request):
    query = request.query_params
    if (
        query.get("hub.mode") == "subscribe"
        and query.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return int(query.get("hub.challenge"))
    return "Verification failed"


# 2. Webhook receiver (POST)
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    print("Incoming Webhook:", data)  # Debug log

    # Extract message text + sender
    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        user_id = message["from"]  # phone number
        text_in = message["text"]["body"]  # user's message
    except (KeyError, IndexError):
        return "no message"

    # Send a reply
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": user_id,
        "text": {"body": f"Echo: {text_in}"},
    }

    async with httpx.AsyncClient() as client:
        await client.post(
            url,
            json=payload,
            headers={"Authorization": f"Bearer {SYSTEM_USER_ACCESS_TOKEN}"},
        )

    return "ok"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
