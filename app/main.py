import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

import streamlit as st
from agents.lesson_agent import generate_lesson
from agents.quiz_agent import generate_quiz
from agents.slides_agent import generate_slides
from utils.file_utils import save_lesson_md, save_quiz_json, save_slides_pptx

st.set_page_config(page_title="AI Course Content Generator")

st.title("🧠 AI Multi-Agent Course Content Generator")
topic = st.text_input("Enter Topic:", value="Operating Systems")

if st.button("Generate Content"):
    with st.spinner("Generating lesson..."):
        lesson = generate_lesson(topic)
        md_file = save_lesson_md(topic, lesson)

    with st.spinner("Generating quiz..."):
        quiz = generate_quiz(topic)
        json_file = save_quiz_json(topic, quiz)

    with st.spinner("Generating slides..."):
        slides = generate_slides(topic)
        pptx_file = save_slides_pptx(topic, slides)

    st.success("✅ Content Generated!")

    # Display Lesson
    st.subheader("Lesson")
    st.text_area("Lesson Markdown", value=lesson, height=300)

    # Display Quiz JSON
    st.subheader("Quiz (JSON)")
    st.text_area("Quiz JSON", value=str(quiz), height=200)

    # Display Slides Text
    st.subheader("Slides Preview")
    st.text_area("Slides Text", value=slides, height=200)

    st.markdown(f"**Files Saved:**")
    st.write(md_file)
    st.write(json_file)
    st.write(pptx_file)

    # Convert string paths to Path objects for download buttons
    md_file_path = Path(md_file)
    json_file_path = Path(json_file)
    pptx_file_path = Path(pptx_file)

    # Download buttons
    with open(md_file_path, "rb") as file:
        st.download_button(
            label="Download Lesson Markdown",
            data=file,
            file_name=md_file_path.name,
            mime="text/markdown"
        )

    with open(json_file_path, "rb") as file:
        st.download_button(
            label="Download Quiz JSON",
            data=file,
            file_name=json_file_path.name,
            mime="application/json"
        )

    with open(pptx_file_path, "rb") as file:
        st.download_button(
            label="Download Slides PPTX",
            data=file,
            file_name=pptx_file_path.name,
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
