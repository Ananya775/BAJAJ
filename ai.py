import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def ask_ai(question: str) -> str:
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not set")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-pro:generateContent?key=" + GEMINI_API_KEY
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": question + " Answer in one word only."
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()

    result = response.json()
    text = result["candidates"][0]["content"]["parts"][0]["text"]

    return text.strip().split()[0]
