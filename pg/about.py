# --- about.py ---
import streamlit as st

def show():
    st.title("📘 About This Project")
    st.markdown("""
    ## 💡 Overview
    **Heart Disease Predictor** is an interactive web application designed to empower individuals and healthcare professionals with advanced tools to assess and understand heart disease risk using machine learning and real health data.

    ## 🔍 Key Features
    - **💓 Risk Prediction**: Input patient data and receive an instant, personalized heart disease risk prediction.
    - **📊 Interactive Insights**: Explore trends, correlations, and severity distributions within heart health data using interactive visualizations.
    - **🧠 Custom Model Trainer**: Choose between Random Forest, SVM, or KNN to train and evaluate your own predictive model with performance metrics.
    - **🧾 Report Generator**: Create and download a professional PDF report summarizing your results.
    - **📖 Educational Tools**: Learn about heart health through facts, prevention tips, quizzes, and visual guides.
    - **📈 Health Progress Tracker**: Log your vitals over time (weight, blood pressure, cholesterol) and visualize your health journey.

    ## 🧠 Models Supported
    - **Random Forest**
    - **Support Vector Machine (SVM)**
    - **K-Nearest Neighbors (KNN)**

    ## 🧪 Dataset Summary
    - Source: Kaggle
    - Records: 920 patient entries
    - Features: Age, Gender, Cholesterol, Chest Pain Type, Blood Pressure, etc.
    - Target: Presence of heart disease (binary classification)

    ## 🔁 Application Workflow
    1. Load and preproce
    ss health data
    2. Train or select a machine learning model
    3. Enter patient details for prediction
    4. Visualize insights and simulation outcomes
    5. Download comprehensive health reports
    6. Track health metrics over time

    ## 🚀 Future Enhancements
    - User login for personal history tracking
    - Integration with wearable devices
    - Deployment as a cross-platform mobile app
    """)
