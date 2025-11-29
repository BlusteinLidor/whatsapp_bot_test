# Example Button Actions for WhatsApp Bot

# 1. PRODUCTIVITY BUTTONS
def productivity_buttons():
    """
    if selected == "reminder":
        send_whatsapp_message(user, "⏰ *Reminder Set*\nI'll remind you about this in 1 hour!")
        # You could integrate with a task scheduler here
        return

    if selected == "todo":
        todo_response = ask_gpt("Create a simple daily todo list with 5 productive tasks")
        send_whatsapp_message(user, f"✅ *Your Todo List:*\n{todo_response}")
        return
    """


# 2. ENTERTAINMENT BUTTONS
def entertainment_buttons():
    """
    if selected == "riddle":
        riddle = ask_gpt("Give me a fun riddle with the answer")
        send_whatsapp_message(user, f"🧩 *Riddle Time:*\n{riddle}")
        return

    if selected == "story":
        story = ask_gpt("Write a very short 2-paragraph interesting story")
        send_whatsapp_message(user, f"📚 *Mini Story:*\n{story}")
        return
    """


# 3. UTILITY BUTTONS
def utility_buttons():
    """
    if selected == "qr_code":
        send_whatsapp_message(user, "📱 *QR Code Generator*\nSend me text and I'll help you create a QR code!")
        return

    if selected == "password":
        password = ask_gpt("Generate a strong, secure password with mix of letters, numbers and symbols")
        send_whatsapp_message(user, f"🔐 *Secure Password:*\n`{password}`\n\n⚠️ Save this safely!")
        return
    """


# 4. LEARNING BUTTONS
def learning_buttons():
    """
    if selected == "word_day":
        word = ask_gpt("Teach me an interesting English word with definition and example")
        send_whatsapp_message(user, f"📖 *Word of the Day:*\n{word}")
        return

    if selected == "tip":
        tip = ask_gpt("Give me a useful life tip or productivity hack")
        send_whatsapp_message(user, f"💡 *Pro Tip:*\n{tip}")
        return
    """


# 5. INTERACTIVE BUTTONS (Save user state)
def interactive_buttons():
    """
    # You could save user preferences/state in a simple dict or database
    user_data = {}

    if selected == "quiz":
        quiz = ask_gpt("Create a fun multiple choice question with 3 options A, B, C")
        user_data[user] = {"mode": "quiz", "question": quiz}
        send_buttons(
            user,
            f"🧠 *Quiz Time:*\n{quiz}",
            [
                {"type": "reply", "reply": {"id": "answer_a", "title": "A"}},
                {"type": "reply", "reply": {"id": "answer_b", "title": "B"}},
                {"type": "reply", "reply": {"id": "answer_c", "title": "C"}},
            ],
        )
        return
    """
