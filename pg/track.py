import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import datetime
from sklearn.linear_model import LinearRegression

# Dummy data initialization
# Create a simple DataFrame to store user health data over time
def init_progress_data():
    return pd.DataFrame(columns=['Date', 'Weight (kg)', 'Cholesterol (mg/dl)', 'Blood Pressure (mmHg)', 'Blood Sugar (mg/dl)', 'Heart Rate (bpm)'])


def save_progress_data(df):
    if 'health_data' in st.session_state:
        # Concatenate the new data (df) with the existing health_data
        st.session_state['health_data'] = pd.concat([st.session_state['health_data'], df], ignore_index=True)
    else:
        st.session_state['health_data'] = df


# Track health metrics page
def show():
    st.title("📊 Health Progress Tracker")

    # Initialize or load existing progress data
    if 'health_data' not in st.session_state:
        st.session_state['health_data'] = init_progress_data()

    # Show user's health progress data
    st.subheader("📅 Track Your Health Over Time")
    
    # Form for entering health data
    with st.form("track_data_form"):
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=400, value=200)
        blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=90, max_value=200, value=120)
        blood_sugar = st.number_input("Blood Sugar (mg/dl)", min_value=50, max_value=300, value=100)
        heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=75)
        submit_button = st.form_submit_button("Track Data")

        # When form is submitted
        if submit_button:
            new_data = pd.DataFrame({
                'Date': [datetime.datetime.now().strftime('%Y-%m-%d')],
                'Weight (kg)': [weight],
                'Cholesterol (mg/dl)': [cholesterol],
                'Blood Pressure (mmHg)': [blood_pressure],
                'Blood Sugar (mg/dl)': [blood_sugar],
                'Heart Rate (bpm)': [heart_rate]
            })
            save_progress_data(new_data)
            st.success("📈 Health data tracked successfully!")

    # Display historical data if available
    if not st.session_state['health_data'].empty:
        st.subheader("📅 Your Health Data History")
        st.write(st.session_state['health_data'])
        
        # Show line graphs for each health metric
        metrics = ['Weight (kg)', 'Cholesterol (mg/dl)', 'Blood Pressure (mmHg)', 'Blood Sugar (mg/dl)', 'Heart Rate (bpm)']
        for metric in metrics:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(pd.to_datetime(st.session_state['health_data']['Date']), st.session_state['health_data'][metric], marker='o', label=metric)
            ax.set_xlabel("Date")
            ax.set_ylabel(metric)
            ax.set_title(f"Trends in {metric} Over Time")
            ax.legend()
            st.pyplot(fig)
        
        # Linear regression analysis for trends
        st.subheader("📈 Predictive Analysis of Your Health Trends")
        metric_to_predict = st.selectbox("Choose a health metric to predict", metrics)
        if metric_to_predict:
            df = st.session_state['health_data']
            df['Date'] = pd.to_datetime(df['Date']).map(datetime.datetime.toordinal)
            X = df[['Date']].values
            y = df[metric_to_predict].values

            model = LinearRegression()
            model.fit(X, y)
            future_dates = pd.date_range(start=df['Date'].max(), periods=30).map(datetime.datetime.toordinal)
            future_predictions = model.predict(future_dates.values.reshape(-1, 1))

            future_dates = pd.to_datetime(future_dates)
            future_df = pd.DataFrame({metric_to_predict: future_predictions}, index=future_dates)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df['Date'], df[metric_to_predict], label="Historical Data", color='blue')
            ax.plot(future_df.index, future_df[metric_to_predict], label="Predicted Data", color='red', linestyle='--')
            ax.set_title(f"Prediction of {metric_to_predict} Over the Next 30 Days")
            ax.set_xlabel("Date")
            ax.set_ylabel(metric_to_predict)
            ax.legend()
            st.pyplot(fig)

    # Set health reminders
    st.subheader("⏰ Health Reminders")
    reminder_time = st.time_input("Set reminder time", value=datetime.time(7, 30))
    reminder_message = st.text_area("Reminder Message", "Time to check your blood pressure!")
    if st.button("Set Reminder"):
        st.session_state["reminder_time"] = reminder_time
        st.session_state["reminder_message"] = reminder_message
        st.success(f"🔔 Reminder set for {reminder_time} - {reminder_message}")

    # Custom Alerts for Health Metrics
    st.subheader("🚨 Health Alerts")
    alert_level = st.selectbox("Choose Alert Level", ['Low', 'Medium', 'High'])
    if st.button("Check Alerts"):
        # Example: Alert based on cholesterol level
        if alert_level == "High":
            if st.session_state['health_data']["Cholesterol (mg/dl)"].iloc[-1] > 240:
                st.warning("⚠ High cholesterol detected! Please consult a healthcare provider.")
            if st.session_state['health_data']["Blood Pressure (mmHg)"].iloc[-1] > 140:
                st.warning("⚠ High blood pressure detected! Please consult a healthcare provider.")
            else:
                st.success("Your metrics are within a safe range.")
                
    # Option to export data
    st.subheader("📤 Export Your Health Data")
    export_button = st.download_button("Download CSV", st.session_state['health_data'].to_csv(index=False), "health_data.csv", "text/csv")
    if export_button:
        st.success("📥 Data exported successfully!")

