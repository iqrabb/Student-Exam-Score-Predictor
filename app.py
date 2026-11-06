import streamlit as st
import pandas as pd
import joblib
import os

from pathlib import Path

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Student Exam Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# Custom CSS (Professional Blue Theme)
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* App background */
.stApp{
    background: linear-gradient(180deg, #EEF3FC 0%, #F8FAFC 100%);
}

/* Hide default Streamlit chrome for a cleaner look */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Header banner */
.header-banner{
    background: linear-gradient(135deg, #1E40AF 0%, #2563EB 55%, #3B82F6 100%);
    padding: 2.2rem 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);
    margin-bottom: 1.8rem;
}

.header-banner h1{
    color: #FFFFFF;
    font-size: 2.3rem;
    font-weight: 800;
    margin-bottom: 0.4rem;
}

.header-banner p{
    color: #DBEAFE;
    font-size: 1.05rem;
    font-weight: 400;
    margin: 0;
}

/* Section card */
.section-card{
    background: #FFFFFF;
    padding: 1.8rem 2rem;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(15, 23, 42, 0.06);
    border: 1px solid #E5EDFB;
    margin-bottom: 1.5rem;
}

.section-title{
    color: #1E3A8A;
    font-weight: 700;
    font-size: 1.15rem;
    margin-bottom: 1rem;
    border-left: 5px solid #2563EB;
    padding-left: 0.7rem;
}

/* Buttons */
.stButton>button{
    width: 100%;
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
    color: white;
    border: none;
    border-radius: 12px;
    height: 52px;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 0.3px;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
    transition: all 0.25s ease-in-out;
}

.stButton>button:hover{
    background: linear-gradient(135deg, #1D4ED8, #1E40AF);
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(37, 99, 235, 0.45);
}

/* Metric card */
[data-testid="stMetric"]{
    background: #FFFFFF;
    border: 1px solid #DBEAFE;
    border-radius: 16px;
    padding: 1.2rem;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.10);
}

[data-testid="stMetricLabel"]{
    color: #1E40AF;
    font-weight: 600;
}

[data-testid="stMetricValue"]{
    color: #1D4ED8;
    font-weight: 800;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #1E3A8A 0%, #1E40AF 100%);
}

section[data-testid="stSidebar"] * {
    color: #F1F5F9 !important;
}

section[data-testid="stSidebar"] hr{
    border-color: rgba(255,255,255,0.2);
}

/* Slider labels */
label{
    color: #1E3A8A !important;
    font-weight: 600 !important;
}

/* Footer */
.footer-box{
    text-align: center;
    padding: 1.2rem;
    margin-top: 1.5rem;
    border-radius: 14px;
    background: #1E3A8A;
    color: #DBEAFE;
    font-size: 0.9rem;
}

.footer-box b{
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# Load Model
# ==================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "student_exam_predictor.pkl"

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model file student_exam_predictor.pkl was not found beside app.py.")
    st.stop()
except Exception as exc:
    st.error("The model file could not be loaded. Check that it is a valid, compatible artifact.")
    st.caption(f"Technical detail: {exc}")
    st.stop()

# ==================================================
# Sidebar
# ==================================================

st.sidebar.image(
    "https://img.icons8.com/color/96/artificial-intelligence.png",
    width=90
)

st.sidebar.title("🎓 Student Exam Predictor")

st.sidebar.markdown("---")

st.sidebar.info("""
Welcome to the **Student Exam Score Prediction System**.

This ML application predicts a student's exam score based on factors like:
• Learning Mode
• Subject
• Study Hours
• Retention Score
• Focus Level

Enter details  and click **Predict Exam Score** to get the prediction.
""")


# ==================================================
# Header Banner
# ==================================================

st.markdown("""
<div class="header-banner">
    <h1>🎓 Student Exam Score Prediction</h1>
    <p>Predict the expected Exam Score using a trained Random Forest Regression Model</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# Input Section
# ==================================================

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📋 Enter Student Details</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    learning_mode = st.selectbox(
        "Learning Mode",
        ["Offline", "Online"]
    )

    study_hours = st.slider(
        "Study Hours",
        1.0,
        8.0,
        4.5,
        0.1
    )

    retention_score = st.slider(
        "Retention Score",
        40,
        100,
        70
    )

with right:

    subject = st.selectbox(
        "Subject",
        [
            "English",
            "History",
            "Math",
            "Programming",
            "Science"
        ]
    )

    focus_level = st.slider(
        "Focus Level",
        40,
        100,
        70
    )

st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# Encoding
# ==================================================

learning_dict = {
    "Offline": 0,
    "Online": 1
}

subject_dict = {
    "English": 0,
    "History": 1,
    "Math": 2,
    "Programming": 3,
    "Science": 4
}

# ==================================================
# Prediction
# ==================================================

if st.button("🎯 Predict Exam Score"):

    data = pd.DataFrame({

        "Learning_Mode": [learning_dict[learning_mode]],
        "Subject": [subject_dict[subject]],
        "Study_Hours": [study_hours],
        "Retention_Score": [retention_score],
        "Focus_Level": [focus_level]

    })

    prediction = float(model.predict(data)[0])

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Prediction Result</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric(
            label="Predicted Exam Score",
            value=f"{prediction:.2f}"
        )

    with col2:
        st.progress(max(0, min(int(prediction), 100)))

        if prediction >= 90:
            st.success("🌟 Outstanding Performance!")
            st.balloons()

        elif prediction >= 80:
            st.success("🎉 Excellent Performance!")

        elif prediction >= 70:
            st.info("😊 Good Performance!")

        elif prediction >= 50:
            st.warning("📚 Average Performance")

        else:
            st.error("❌ Needs Improvement")

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# Footer
# ==================================================

st.markdown("""
<div class="footer-box">
    Developed by <b>Iqra ❤️</b><br>
    AI Learner &nbsp;|&nbsp; Machine Learning Project
</div>
""", unsafe_allow_html=True)