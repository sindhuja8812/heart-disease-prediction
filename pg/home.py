import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

def show():
    # Load Logo
    logo = Image.open("assets/heart_home.png")

    # Layout: Logo at top left
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(logo, width=160)  # Increased logo size

    # Red Gradient Box with Centered Content
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f8d7da, #f5c2c7);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        ">
            <h1 style="color: #b02a37; font-size: 3.5rem;">🫀 Heart Disease Risk Prediction</h1>
            <p style="font-size: 2rem; color: #333;">
                Welcome to the <b>Heart Disease Predictor</b> – a powerful tool to assess your heart disease risk using real health data and machine learning.
            </p>
            <hr style="border: 1px solid #b02a37;">
            <div style="text-align: left; padding: 0 1rem; max-width: 800px; margin: auto;">
                <ul style="font-size: 1.5rem; line-height: 2.2; color: #444;">
                    <li><b>🧠 Learn:</b> Explore heart disease facts, symptoms, and prevention.</li>
                    <li><b>📊 Explore:</b> Discover insights from real-world health datasets.</li>
                    <li><b>🔍 Predict:</b> Get a personalized risk prediction instantly.</li>
                    <li><b>📝 Report:</b> Download a professional PDF summary of your result.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
            <div style='background-color: #e0f3ff; padding: 1.5rem; border-radius: 10px; max-width: 1000px; margin: auto;'>
                <span style='font-size: 1.6rem; color: #31708f;'>💡 Use the sidebar to navigate between pages</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
