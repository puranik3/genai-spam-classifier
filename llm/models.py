import os
from langchain_google_genai import ChatGoogleGenerativeAI
from config import gemini_api_key, DEFAULT_MODEL, temp


def get_llm():
    if not gemini_api_key:
        raise RuntimeError("Missing API Keys")

    return ChatGoogleGenerativeAI(
        model = DEFAULT_MODEL,
        google_api_key = gemini_api_key,
        temperature = temp
    )
