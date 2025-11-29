# whatsapp.py
import requests
import os

TOKEN = os.getenv("SYSTEM_USER_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


def send_whatsapp_message(to: str, text: str):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text},
    }
    headers = {"Authorization": f"Bearer {TOKEN}"}

    res = requests.post(url, json=payload, headers=headers)
    return res.json()


def send_buttons(to: str, body: str, buttons: list):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": body},
            "action": {"buttons": buttons},
        },
    }
    headers = {"Authorization": f"Bearer {TOKEN}"}
    return requests.post(url, json=payload, headers=headers).json()


def send_list(to, body, items):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {"text": body},
            "action": {"button": "Open Menu", "sections": items},
        },
    }
    headers = {"Authorization": f"Bearer {TOKEN}"}
    return requests.post(url, json=payload, headers=headers).json()
