from utils.llm import generate_with_fallback
from utils.prompt_templates import LESSON_PROMPT

def generate_lesson(topic: str) -> str:
    prompt = LESSON_PROMPT.format(topic=topic)
    return generate_with_fallback(prompt)
