import streamlit as st
from preprocess import clean_text
from vectorize import vectorize_text
from similarity import compute_similarity

st.set_page_config(page_title="AI Resume Screening", layout="centered")

# ----------- CLEAN CSS (NO EXTRA RECTANGLE) -----------
st.markdown("""
<style>

/* Page background */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}

/* Remove extra blank blocks */
section.main > div {
    padding-top: 2rem;
}

/* Center content width */
.block-container {
    max-width: 800px;
}

/* Title */
h1 {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 30px;
}

/* Purple gradient button */
.stButton>button {
    background: linear-gradient(90deg, #6a5acd, #8a63ff);
    color: white;
    font-size: 18px;
    font-weight: 600;
    padding: 12px 40px;
    border-radius: 12px;
    border: none;
    display: block;
    margin: 25px auto 0 auto;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #5a4bcc, #7a52ff);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------
st.title("📄 AI Resume Screening System")
st.markdown("<div class='subtitle'>Upload a resume and compare it with a job description</div>", unsafe_allow_html=True)

# ----------- FORM -----------
uploaded_resume = st.file_uploader("Upload Resume (TXT format)", type=["txt"])
job_description = st.text_area("Paste Job Description", height=200)

analyze = st.button("Analyze Resume")

if analyze:
    if uploaded_resume is None or job_description.strip() == "":
        st.error("Please upload a resume and provide a job description.")
    else:
        resume_text = uploaded_resume.read().decode("utf-8")

        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)

        resume_vectors, jd_vector = vectorize_text([clean_resume], clean_jd)
        score = compute_similarity(resume_vectors, jd_vector)[0] * 100

        st.success("Analysis Complete")
        st.metric("Resume Match Score", f"{score:.2f} %")