import streamlit as st

from resume_parser import extract_text_from_pdf
from matcher import match_resume


st.title("🤖 AI Resume Analyzer & Job Matcher")

st.write(
    "Upload your resume and paste a job description "
    "to analyze your compatibility."
)


resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description"
)


if st.button("Analyze Resume"):

    if resume and job_description:

        resume_text = extract_text_from_pdf(resume)

        result = match_resume(
            resume_text,
            job_description
        )

        st.subheader("Match Score")

        st.metric(
            "Compatibility",
            f"{result['score']}%"
        )

        st.subheader("Matched Skills")

        for skill in result["matched"]:
            st.write("✅", skill)

        st.subheader("Missing Skills")

        for skill in result["missing"]:
            st.write("❌", skill)

    else:

        st.warning(
            "Please upload a resume and enter a job description."
        )