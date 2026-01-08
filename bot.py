import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


def process_message(text: str, mode: str) -> str:
    if mode == "grammar":
        system_prompt = (
            "You are an English grammar correction assistant. "
            "Correct the user's sentence. "
            "Return ONLY the corrected sentence. "
            "Do not explain anything."
        )
    else:  # chat mode
        system_prompt = (
            "You are a friendly English assistant. "
            "Talk naturally, answer questions, and help clarify doubts."
        )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
