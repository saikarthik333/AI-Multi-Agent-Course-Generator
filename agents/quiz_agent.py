from utils.llm import generate_with_fallback
from utils.prompt_templates import QUIZ_PROMPT
import json

def generate_quiz(topic: str) -> dict:
    prompt = QUIZ_PROMPT.format(topic=topic)
    response = generate_with_fallback(prompt)
    
    try:
        quiz_data = json.loads(response)
        return quiz_data
    except:
        # If not valid JSON, just return raw text
        return {"raw_text": response}
