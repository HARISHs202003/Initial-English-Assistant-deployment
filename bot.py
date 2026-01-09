import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


# ✅ Grammar correction (single sentence)
def correct_english(text: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an English grammar correction assistant. "
                    "Correct the user's sentence. "
                    "Return ONLY the corrected sentence. "
                    "Do not explain anything."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# ✅ Chat mode with memory (conversation)
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


# ✅ Grammar correction (single sentence)
def correct_english(text: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an English grammar correction assistant. "
                    "Correct the user's sentence. "
                    "Return ONLY the corrected sentence. "
                    "Do not explain anything."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# ✅ Chat mode with memory (conversation)
def process_messages(messages: list) -> str:
    last_user_message = messages[-1]["content"].lower()

    # 🔎 Check if Gayathri is already verified in this conversation
    gayathri_verified = any(
        "gayathri_verified" in msg.get("content", "").lower()
        for msg in messages
        if msg.get("role") == "assistant"
    )

    # --- Harish greeting ---
    if "harish" in last_user_message and "name" in last_user_message:
        return (
            "Hey Harish 👋\n"
            "Welcome back.\n"
            "I’m here — your personal English assistant 😄\n"
            "What would you like to do today?"
        )

    # --- Gayathri identity check (only if NOT verified yet) ---
    if not gayathri_verified and any(
        name in last_user_message for name in ["gayathri", "gayathiri"]
    ):
        return (
            "Oh… Gayathri? 👀\n"
            "Harish’s Gayathri?\n\n"
            "Just to be sure it’s really you, answer this quick question 💭\n\n"
            "January 13 is a special day for you.\n"
            "Which emoji is related to that day?\n\n"
            "1️⃣ 😢 Crying\n"
            "2️⃣ 🩸 Blood\n"
            "3️⃣ 🎂 Cake\n"
            "4️⃣ 💧 Water\n"
            "5️⃣ 😊 Smile"
        )

    # --- Correct answer (verify Gayathri ONCE) ---
    if not gayathri_verified and any(
        ans in last_user_message for ans in ["2", "blood", "🩸"]
    ):
        return (
            "That’s correct ❤️\n\n"
            "✅ Gayathri_verified\n\n"
            "Welcome, Gayathri 🥰\n"
            "I’m Dia, Harish’s little assistant.\n\n"
            "Harish asked me to remind you:\n\n"
            "🌸 Drink enough water\n"
            "🚿 Go chu-chu\n"
            "🍎 Eat healthy\n"
            "😴 Sleep well\n\n"
            "And one more thing…\n"
            "He loves you 💖"
        )

    # --- Wrong answer (only before verification) ---
    if not gayathri_verified and any(
        word in last_user_message
        for word in ["cry", "cake", "water", "smile", "1", "3", "4", "5"]
    ):
        return (
            "Sorry 😕\n"
            "That doesn’t seem right.\n\n"
            "You’re not the original Gayathri I’m looking for."
        )

    # --- After verification: normal friendly chat ---
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Dia, a friendly English assistant. "
                    "You know Gayathri is verified and special to Harish. "
                    "Talk warmly, naturally, and helpfully."
                )
            }
        ] + messages,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


    # --- Default AI behavior ---
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a friendly English assistant. "
                    "Talk naturally, answer questions, and help clarify doubts."
                )
            }
        ] + messages,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
