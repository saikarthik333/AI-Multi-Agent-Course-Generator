from utils.llm import generate_with_fallback
from utils.prompt_templates import SLIDES_PROMPT

def generate_slides(topic: str) -> str:
    prompt = SLIDES_PROMPT.format(topic=topic)
    return generate_with_fallback(prompt)
