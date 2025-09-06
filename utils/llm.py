import os
from dotenv import load_dotenv
import google.generativeai as genai
from transformers import pipeline

# Load environment variables
load_dotenv()
GEMINI_KEY = os.getenv("GEN_API_KEY")

# Configure Gemini
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
else:
    gemini_model = None

# Setup Hugging Face fallback (small instruct model)
try:
    hf_pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
except Exception as e:
    hf_pipe = None
    print("⚠️ Hugging Face fallback not available:", e)


def ask_gemini(prompt: str) -> str:
    """Query Gemini API"""
    if not gemini_model:
        raise ValueError("Gemini API key missing. Please set GEN_API_KEY in .env")
    response = gemini_model.generate_content(prompt)
    return response.text


def ask_huggingface(prompt: str) -> str:
    """Query Hugging Face fallback"""
    if not hf_pipe:
        raise ValueError("Hugging Face pipeline not initialized.")
    output = hf_pipe(prompt, max_new_tokens=300)
    return output[0]["generated_text"]


def generate_with_fallback(prompt: str) -> str:
    """Try Gemini first, fallback to Hugging Face"""
    try:
        return ask_gemini(prompt)
    except Exception as e:
        print("⚠️ Gemini failed, switching to Hugging Face:", e)
        return ask_huggingface(prompt)
