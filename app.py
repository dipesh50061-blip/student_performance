import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# Load Trained Model
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "student_performance_model.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Performance Predictor")
st.write(
    "Enter the student's information below to predict their expected performance."
)

st.divider()


# -----------------------------
# Student Information
# -----------------------------
st.subheader("📋 Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=10,
        max_value=30,
        value=18
    )

    study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=5.0
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    previous_score = st.number_input(
        "Previous Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )


with col2:
    assignments_completed = st.number_input(
        "Assignments Completed",
        min_value=0,
        max_value=100,
        value=10
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0
    )

    internet_access = st.selectbox(
        "Internet Access",
        ["Yes", "No"]
    )

    parent_education = st.selectbox(
        "Parent Education",
        ["Graduate", "Postgraduate", "High School", "Other"]
    )

    extra_activities = st.selectbox(
        "Extra Activities",
        ["Yes", "No"]
    )


with col3:
    family_income = st.selectbox(
        "Family Income",
        ["Low", "Medium", "High"]
    )

    class_participation = st.number_input(
        "Class Participation",
        min_value=0,
        max_value=10,
        value=5
    )

    study_method = st.selectbox(
        "Study Method",
        ["Self Study", "Group Study", "Online", "Coaching"]
    )

    stress_level = st.number_input(
        "Stress Level",
        min_value=0,
        max_value=10,
        value=5
    )


st.divider()


# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔮 Predict Performance", use_container_width=True):

    new_student = pd.DataFrame({
        "gender": [gender],
        "age": [age],
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_score": [previous_score],
        "assignments_completed": [assignments_completed],
        "sleep_hours": [sleep_hours],
        "internet_access": [internet_access],
        "parent_education": [parent_education],
        "extra_activities": [extra_activities],
        "family_income": [family_income],
        "class_participation": [class_participation],
        "study_method": [study_method],
        "stress_level": [stress_level]
    })

    # Prediction
    prediction = model.predict(new_student)[0]

    # Probability
    probabilities = model.predict_proba(new_student)[0]
    classes = model.classes_

    # -----------------------------
    # Result
    # -----------------------------
    st.success(f"🎯 Predicted Performance: **{prediction}**")

    st.subheader("📊 Prediction Probabilities")

    probability_df = pd.DataFrame({
        "Performance": classes,
        "Probability": probabilities
    })

    probability_df["Probability"] = (
        probability_df["Probability"] * 100
    ).round(2)

    st.bar_chart(
        probability_df.set_index("Performance")
    )

    st.dataframe(
        probability_df,
        use_container_width=True
    )