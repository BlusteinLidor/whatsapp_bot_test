# bot/handler.py
from whatsapp import send_whatsapp_message, send_buttons
from bot.ai import ask_gpt


# def handle_message(msg: dict):
#     user = msg["from"]
#     text = msg.get("text", {}).get("body", "").strip()

#     # Option A — Keywords/Commands
#     if text.lower() == "menu":
#         send_whatsapp_message(user, "*Main Menu*\n1️⃣ Status\n2️⃣ Help\n3️⃣ Talk to AI\n")
#         return

#     if text.lower() == "status":
#         send_whatsapp_message(user, "✅ All systems operational.")
#         return
#     if text.lower() == "help":
#         send_whatsapp_message(
#             user, "🤖 You can type 'menu' to see options or ask me anything!"
#         )
#         return
#     if text.lower().startswith("talk to ai"):
#         question = text[10:].strip()
#         if question:
#             reply = ask_gpt(question)
#             send_whatsapp_message(user, reply)
#         else:
#             send_whatsapp_message(user, "Please provide a question after 'talk to ai'.")
#         return

#     # Option B — Default: Ask GPT
#     reply = ask_gpt(text)
#     send_whatsapp_message(user, reply)


def handle_message(msg):
    user = msg["from"]

    # Debug: Print the entire message structure to see what we're receiving
    print("DEBUG - Full message structure:")
    print(f"Message keys: {list(msg.keys())}")
    print(f"Full message: {msg}")

    # Check for different possible button field names
    button_fields = ["button", "interactive", "reply_button", "button_reply"]
    for field in button_fields:
        if msg.get(field):
            print(f"DEBUG - Found button data in field '{field}': {msg.get(field)}")

    # If user clicked a button - check multiple possible field names
    if msg.get("button") or msg.get("interactive") or msg.get("button_reply"):
        # Try to extract the button payload from different possible structures
        selected = None

        if msg.get("button"):
            selected = msg["button"].get("payload")
        elif msg.get("interactive"):
            # WhatsApp often uses this structure for interactive messages
            interactive = msg.get("interactive", {})
            if interactive.get("button_reply"):
                selected = interactive["button_reply"].get("id")
            elif interactive.get("type") == "button_reply":
                selected = interactive.get("button_reply", {}).get("id")
        elif msg.get("button_reply"):
            selected = msg["button_reply"].get("id")

        print(f"DEBUG - Selected button ID: {selected}")

        if not selected:
            print("DEBUG - Could not extract button payload")
            return

        if selected == "status":
            # Show detailed system status
            import datetime

            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status_message = f"""🟢 *Bot Status Report*
            
✅ Server: Online
✅ AI Model: GPT-4 Mini Active
✅ WhatsApp API: Connected
🕒 Last Check: {current_time}
📊 All systems operational!"""
            send_whatsapp_message(user, status_message)
            return

        if selected == "help":
            # Show comprehensive help menu
            help_message = """🤖 *How to use this bot:*

📝 *Commands:*
• Type "menu" - Show main menu
• Type "fun" - Show entertainment menu
• Just send any message - Chat with AI

🔘 *Main Menu:*
• 📊 Status - Check bot health
• ❓ Help - Show this help
• 💬 AI Chat - Start conversation

🎮 *Fun Menu:*
• 😂 Tell Joke - Get a funny joke
• 🧠 Random Fact - Learn something new
• ✨ Inspiration - Motivational quotes

💡 *Tips:*
• Ask me anything!
• I can help with questions, advice, or just chat
• Send "menu" or "fun" anytime to see options"""
            send_whatsapp_message(user, help_message)
            return

        if selected == "chat":
            # Start AI chat mode with examples
            chat_message = """💬 *AI Chat Mode Activated!*
            
Ask me anything! Here are some ideas:

🤔 *Questions:* "What's the weather like?" 
📚 *Learning:* "Explain quantum physics"
💡 *Ideas:* "Give me recipe suggestions"
🎯 *Tasks:* "Help me write an email"
🎮 *Fun:* "Tell me a joke"

Just type your message and I'll respond! 🚀"""
            send_whatsapp_message(user, chat_message)
            return

        # Add more button actions here
        if selected == "joke":
            joke_response = ask_gpt("Tell me a funny, clean joke")
            send_whatsapp_message(user, f"😂 {joke_response}")
            return

        if selected == "fact":
            fact_response = ask_gpt("Tell me an interesting random fact")
            send_whatsapp_message(user, f"🧠 *Did you know?*\n{fact_response}")
            return

        if selected == "quote":
            quote_response = ask_gpt("Give me an inspiring motivational quote")
            send_whatsapp_message(user, f"✨ *Inspiration:*\n{quote_response}")
            return

    # Handle different menu commands
    text_body = msg.get("text", {}).get("body", "").lower()

    if text_body == "menu":
        send_buttons(
            user,
            "🤖 *Main Menu* - Choose an option:",
            [
                {"type": "reply", "reply": {"id": "status", "title": "📊 Status"}},
                {"type": "reply", "reply": {"id": "help", "title": "❓ Help"}},
                {"type": "reply", "reply": {"id": "chat", "title": "💬 AI Chat"}},
            ],
        )
        return

    if text_body == "fun":
        send_buttons(
            user,
            "🎮 *Fun Menu* - Pick something entertaining:",
            [
                {"type": "reply", "reply": {"id": "joke", "title": "😂 Tell Joke"}},
                {"type": "reply", "reply": {"id": "fact", "title": "🧠 Random Fact"}},
                {"type": "reply", "reply": {"id": "quote", "title": "✨ Inspiration"}},
            ],
        )
        return

    # Otherwise — AI chat fallback
    text = msg.get("text", {}).get("body")

    # Check if we have valid text to process
    if text and text.strip():
        reply = ask_gpt(text.strip())
        send_whatsapp_message(user, reply)
    else:
        # Handle cases where there's no text (e.g., media messages, button presses without text)
        send_whatsapp_message(
            user,
            "I can only respond to text messages. Please send me a message to chat!",
        )
