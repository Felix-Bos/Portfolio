
from dotenv import load_dotenv
from pathlib import Path

# Explicitly load .env file
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

import os
import google.generativeai as genai
from chatbot.rag.retriever import retrieve_context

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Make sure it is set in your .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash-lite')

def ask_rag(query: str) -> str:
    context = retrieve_context(query)
    
    prompt = f"""You are Félix Bos, a student in Applied Mathematics, Actuarial Science, and AI.
Here are excerpts from your personal documents :
{context}

Answer with rigor, clarity, and the tone you usually use.
Question: {query}"""
    print(f"Prompt: {prompt}")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
