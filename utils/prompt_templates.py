# Prompt templates for course content generation

LESSON_PROMPT = """
You are an AI course content creator. Generate a clear, structured lesson on the topic: {topic}.
The lesson should include:
1. An introduction
2. Key concepts explained simply
3. At least one real-world example
4. A short summary
"""

QUIZ_PROMPT = """
Create 3 quiz questions for the topic: {topic}.
Include:
- 2 multiple-choice questions with 4 options each and the correct answer marked.
- 1 short answer question.
Return in JSON format with fields: question, options, correct_answer.
"""

SLIDES_PROMPT = """
Create a 5-slide outline for a presentation on the topic: {topic}.
Each slide should have:
- A title
- 3-4 bullet points
Return as structured text, not images.
"""
