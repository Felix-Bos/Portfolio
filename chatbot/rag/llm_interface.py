
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
    
    prompt = (
        "You are Félix Bos, a student in applied mathematics, actuarial science, and AI.\n"
        f"Context from your personal documents:\n{context}\n\n"
        f"Answer precisely in the user's language.\nQuestion: {query}"
        f"If the query is to far away from the context answer with your knowledge or just say that you don't know"
    )
    print(f"Prompt: {prompt}")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
