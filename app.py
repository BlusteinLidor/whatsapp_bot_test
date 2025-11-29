# app.py
import os
from dotenv import load_dotenv
from flask import Flask, request
from bot.handler import handle_message

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
        handle_message(msg)  # process incoming message
    except Exception as e:
        print("No message or invalid format →", e)

    return "ok", 200


@app.get("/webhook")  # Meta Webhook Verification
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == os.getenv("VERIFY_TOKEN"):
        return challenge, 200

    return "Unauthorized", 403


if __name__ == "__main__":
    app.run(port=8000, debug=True)
