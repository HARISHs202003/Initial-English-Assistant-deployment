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
