# 📁 prediction.py

import streamlit as st
import pandas as pd
from utils.preprocessing import preprocess_input
from utils.model import get_prediction, load_model

def show():
    st.title("🩺 Heart Disease Prediction")
    st.markdown("Enter the patient's details below to predict the likelihood of heart disease.")

    model, scaler = load_model()

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=29, max_value=77, value=54)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=90, max_value=200, value=130)
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=245)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])

    with col2:
        restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
        thalch = st.number_input("Max Heart Rate Achieved", min_value=70, max_value=210, value=150)
        exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
        oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=6.2, value=1.0, step=0.1)
        slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
        ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4, value=0)
        thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    if st.button("🔍 Predict"):
        input_dict = {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs == "True",
            "restecg": restecg,
            "thalch": thalch,
            "exang": exang == "Yes",
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }

        input_df = pd.DataFrame([input_dict])
        processed_input = preprocess_input(input_df, scaler)

        pred, confidence = get_prediction(processed_input)

        st.session_state.prediction = pred
        st.session_state.confidence = confidence
        st.session_state.input_data = input_df
        st.session_state.processed_input = processed_input

        if pred == 1:
            st.error(f"⚠️ The model predicts a high risk of heart disease with {confidence:.2f}% confidence.")
        else:
            st.success(f"✅ The model predicts low risk of heart disease with {confidence:.2f}% confidence.")
