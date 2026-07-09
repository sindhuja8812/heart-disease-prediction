import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import joblib
from utils.preprocessing import load_data, preprocess_input
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def show():
    st.title("📊 Advanced Heart Disease Data Insights")

    df = load_data()

    # Encode all object (categorical) columns
    label_encoders = {}
    for col in df.columns:
        if df[col].dtype == 'object':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

    st.markdown("""
    Use the interactive filters and visualizations below to explore the relationship between various health parameters and heart disease.
    """)

    # Sidebar Filters
    st.sidebar.header("🔎 Filter Options")
    age_filter = st.sidebar.slider("Select Age Range", int(df.age.min()), int(df.age.max()), (30, 60))
    sex_filter = st.sidebar.selectbox("Select Gender", options=["All", "Male", "Female"])
    target_filter = st.sidebar.selectbox("Heart Disease", options=["All", "Yes", "No"])

    # Apply Filters
    filtered_df = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]
    if sex_filter != "All":
        filtered_df = filtered_df[filtered_df['sex'] == (1 if sex_filter == "Male" else 0)]
    if target_filter != "All":
        filtered_df = filtered_df[filtered_df['target'] == (1 if target_filter == "Yes" else 0)]

    # Dataset Preview
    st.subheader("📋 Filtered Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True)

    # Age-wise Heart Disease Severity Histogram
    st.subheader("📈 Heart Disease by Age")
    st.markdown("""
    <p style='color:#888; font-size: 1rem;'>Severity scale: 0 = No disease, 1-4 = Increasing severity</p>
    """, unsafe_allow_html=True)

    severity_labels = {0: "No Disease", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Very Severe"}
    if 'target' in filtered_df.columns:
        filtered_df['target'] = filtered_df['target'].replace(severity_labels)

    fig = px.histogram(filtered_df, x="age", color="target", barmode="group", histnorm="percent",
                       labels={"target": "Heart Disease Severity", "age": "Age"},
                       color_discrete_sequence=["#2ca02c", "#ff9999", "#ff6666", "#ff0000", "#8b0000"])
    fig.update_layout(legend_title_text='Heart Disease Severity', xaxis_title="Age", yaxis_title="Percentage")
    st.plotly_chart(fig, use_container_width=True)

    # Correlation Heatmap
    st.subheader("🧬 Feature Correlation with Heart Disease")
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Pie Chart - Gender Distribution
    st.subheader("👥 Gender Distribution")
    pie = px.pie(df, names='sex', title='Gender Distribution', labels={0: 'Female', 1: 'Male'})
    st.plotly_chart(pie, use_container_width=True)

    # Feature Importance
    st.subheader("📌 Most and Least Influential Features")
    st.markdown("Using feature importance from a Random Forest model, we rank which factors most significantly impact the prediction of heart disease.")

    model_df = df.copy()
    X = model_df.drop(columns=["target"])
    y = model_df["target"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    importances = pd.DataFrame({"Feature": X.columns, "Importance": model.feature_importances_})
    importances = importances.sort_values(by="Importance", ascending=False)

    fig2 = px.bar(importances, x="Importance", y="Feature", orientation='h',
                  title="Feature Importance for Heart Disease Prediction",
                  color="Importance", color_continuous_scale="Reds")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    - 🟥 **Most impactful features**: cholesterol, max heart rate, chest pain.
    - 🟦 **Least impactful**: fasting blood sugar, ST slope.
    """)

    # Load model and scaler
    model = joblib.load("models/heart_disease_rf_model.pkl")
    scaler = joblib.load("models/heart_disease_scaler.pkl")

    # Hypothetical Risk Simulation
    X = df.drop("target", axis=1)

    st.subheader("🧪 Hypothetical Risk Simulation")
    st.markdown("Adjust values to simulate how your health affects heart disease risk.")

    with st.expander("🔬 Try Simulating Risk Factor Influence"):
        user_sim = {}

        for col in X.columns:
            if df[col].dtype in [int, float]:
                low = float(df[col].quantile(0.01))
                high = float(df[col].quantile(0.99))
                mean = float(df[col].mean())
                user_sim[col] = st.slider(col.capitalize(), low, high, mean)
            else:
                user_sim[col] = df[col].mode()[0]

        input_df = pd.DataFrame([user_sim])
        input_df = input_df[X.columns]  # Ensure correct order
        processed_input = preprocess_input(input_df, scaler)
        risk_pred = model.predict_proba(processed_input)[0][1] * 100

        st.success(f"🔍 Simulated Heart Disease Risk: {risk_pred:.2f}%")
