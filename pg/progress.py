# --- progress.py ---
import streamlit as st
import pandas as pd
import datetime
import os

PROGRESS_FILE = "progress_tracker.csv"

def show():
    st.title("📈 Track Your Health Progress")
    st.markdown("Log and visualize your vitals over time.")

    # Input section
    with st.form("track_form"):
        st.subheader("🩺 Enter Your Vitals")
        date = st.date_input("Date", datetime.date.today())
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        systolic = st.number_input("Systolic BP", 80, 200, 120)
        diastolic = st.number_input("Diastolic BP", 50, 150, 80)
        cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 400, 200)
        submit = st.form_submit_button("Save Entry")

    if submit:
        entry = pd.DataFrame([[date, weight, systolic, diastolic, cholesterol]],
                             columns=["Date", "Weight", "Systolic", "Diastolic", "Cholesterol"])
        if os.path.exists(PROGRESS_FILE):
            old = pd.read_csv(PROGRESS_FILE)
            data = pd.concat([old, entry], ignore_index=True)
        else:
            data = entry
        data.to_csv(PROGRESS_FILE, index=False)
        st.success("Entry saved!")

    # Display historical data and chart
    if os.path.exists(PROGRESS_FILE):
        st.subheader("📊 Progress Over Time")
        df = pd.read_csv(PROGRESS_FILE, parse_dates=["Date"])
        df.sort_values("Date", inplace=True)

        st.line_chart(df.set_index("Date")[["Weight", "Systolic", "Diastolic", "Cholesterol"]])

        st.dataframe(df.tail(10), use_container_width=True)
        st.download_button("📅 Download CSV", df.to_csv(index=False), file_name="health_progress.csv")

        # Delete an entry
        st.subheader("🗑️ Delete an Entry")
        df["Label"] = df["Date"].astype(str) + " | Weight: " + df["Weight"].astype(str)
        selected = st.selectbox("Select entry to delete:", df["Label"])

        if st.button("❌ Delete Selected Entry"):
            idx_to_drop = df[df["Label"] == selected].index
            df.drop(idx_to_drop, inplace=True)
            df.drop(columns="Label", inplace=True)
            df.to_csv(PROGRESS_FILE, index=False)
            st.success("Entry deleted successfully.")