import sys
from pathlib import Path
import zipfile
import streamlit as st

# Add project root to sys.path
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

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

    # Display previews
    st.subheader("Lesson")
    st.text_area("Lesson Markdown", value=lesson, height=300)

    st.subheader("Quiz (JSON)")
    st.text_area("Quiz JSON", value=str(quiz), height=200)

    st.subheader("Slides Preview")
    st.text_area("Slides Text", value=slides, height=200)

    # Create ZIP of all files
    zip_path = Path("data") / f"{topic.replace(' ', '_')}_content.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(md_file, Path(md_file).name)
        zf.write(json_file, Path(json_file).name)
        zf.write(pptx_file, Path(pptx_file).name)

    # Download button for ZIP
    with open(zip_path, "rb") as file:
        st.download_button(
            "Download All Content (ZIP)",
            data=file,
            file_name=zip_path.name,
            mime="application/zip"
        )

    st.markdown(f"**Individual Files Saved:**")
    st.write(md_file)
    st.write(json_file)
    st.write(pptx_file)
