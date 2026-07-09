# --- model_trainer.py ---

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

import utils.style as style
from utils.preprocessing import load_data

style.apply_custom_css()

model_dict = {
    "Random Forest": RandomForestClassifier,
    "K-Nearest Neighbors": KNeighborsClassifier,
    "Support Vector Machine": SVC
}

def preprocess_training_data(df):
    from utils.preprocessing import ENCODINGS

    df = df.copy()
    for col, mapping in ENCODINGS.items():
        df[col] = df[col].map(mapping)

    df['fbs'] = df['fbs'].astype(int)
    df['exang'] = df['exang'].astype(int)

    X = df.drop('target', axis=1)
    y = df['target']
    return X, y

def show():
    st.title("🧠 Train Your Model")
    st.markdown("Select an algorithm, adjust parameters, and train your custom model.")

    df = load_data()
    X, y = preprocess_training_data(df)

    model_choice = st.selectbox("Choose a model:", list(model_dict.keys()))

    test_size = st.slider("Test set size (%)", 10, 50, 20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)

    st.subheader("🔧 Model Parameters")

    model = None
    if model_choice == "Random Forest":
        n_estimators = st.slider("n_estimators", 10, 200, 100)
        max_depth = st.slider("max_depth", 1, 20, 5)
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

    elif model_choice == "K-Nearest Neighbors":
        n_neighbors = st.slider("n_neighbors", 1, 20, 5)
        model = make_pipeline(
            SimpleImputer(strategy="mean"),
            KNeighborsClassifier(n_neighbors=n_neighbors)
        )

    elif model_choice == "Support Vector Machine":
        kernel = st.selectbox("Kernel", ["linear", "rbf", "poly"])
        C = st.slider("C (regularization)", 0.1, 10.0, 1.0)
        model = make_pipeline(
            SimpleImputer(strategy="mean"),
            SVC(kernel=kernel, C=C, probability=True)
        )

    if st.button("🚀 Train Model"):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.success("Model trained successfully!")

        st.subheader("📈 Performance Metrics")
        acc = accuracy_score(y_test, y_pred)
        st.metric("Accuracy", f"{acc*100:.2f}%")

        st.text("Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        st.pyplot(fig)

        st.text("Classification Report")
        st.code(classification_report(y_test, y_pred), language='text')

        if st.button("💾 Save Model"):
            os.makedirs("trained_models", exist_ok=True)
            model_name = f"trained_models/{model_choice.replace(' ', '_').lower()}_custom_model.pkl"
            joblib.dump(model, model_name)
            st.success(f"Model saved as {model_name}")