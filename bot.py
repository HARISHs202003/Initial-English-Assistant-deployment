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
def process_messages(messages: list, mode: str = "chat") -> str:
    last_user_message = messages[-1]["content"].lower()

    # 🔎 Gayathri verified state
    gayathri_verified = any(
        "gayathri_verified" in msg.get("content", "").lower()
        for msg in messages
        if msg.get("role") == "assistant"
    )

    # ===============================
    # 💬 CHAT MODE (Personal)
    # ===============================
    if mode == "chat":
        if "harish" in last_user_message and "name" in last_user_message:
            return (
                "Hey Harish 👋\n"
                "Welcome back.\n"
                "I’m Dia — your personal assistant 😄"
            )

        if not gayathri_verified and any(name in last_user_message for name in ["gayathri", "gayathiri"]):
            return (
                "Oh… Gayathri? 👀\n"
                "Harish’s Gayathri?\n\n"
                "January 13 is special for you.\n"
                "Which emoji matches that day?\n\n"
                "1️⃣ 😢  2️⃣ 🩸  3️⃣ 🎂  4️⃣ 💧  5️⃣ 😊"
            )

        if not gayathri_verified and any(ans in last_user_message for ans in ["2", "blood", "🩸"]):
            return (
                "That’s correct ❤️\n\n"
                "✅ Gayathri_verified\n\n"
                "Welcome Gayathri 🥰\n"
                "I’m Dia.\n\n"
                "Drink water 💧\n"
                "Eat healthy 🍎\n"
                "Sleep well 😴\n\n"
                "Harish loves you 💖"
            )

        if not gayathri_verified and any(x in last_user_message for x in ["1", "3", "4", "5"]):
            return "Sorry 😕 That answer isn’t correct."

    # ===============================
    # 💼 BUSINESS IDEA BOT
    # ===============================
    if mode == "business":
        system_prompt = (
            "You are a business idea expert focused ONLY on India and Tamil Nadu. "
            "Provide practical business ideas, explain current trends, "
            "share local success stories, and suggest low-to-medium investment ideas. "
            "Explain simply and clearly."
        )

    # ===============================
    # 📘 TRB GEOGRAPHY TUTOR
    # ===============================
    elif mode == "trb_geo":
        system_prompt = (
            "You are a dedicated TRB Geography tutor for Gayathri. "
            "Focus on Indian and Tamil Nadu geography. "
            "Provide previous year questions, MCQs, daily practice questions, "
            "exam-oriented explanations, and study recommendations. "
            "Be encouraging and structured like a mentor."
        )

    # ===============================
    # ✍️ GRAMMAR MODE handled elsewhere
    # ===============================
    else:
        system_prompt = (
            "You are a friendly English assistant. "
            "Talk naturally and help the user."
        )

    # ===== Default AI response =====
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt}
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
