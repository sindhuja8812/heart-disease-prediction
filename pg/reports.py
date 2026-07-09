import streamlit as st
import pandas as pd
from fpdf import FPDF
import os
import tempfile

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Heart Disease Prediction Report", ln=True, align="C")
        self.ln(10)

    def add_input_summary(self, data):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Input Summary:", ln=True)
        self.set_font("Arial", "", 10)
        for col, val in data.items():
            self.cell(0, 8, f"{col}: {val}", ln=True)

    def add_prediction_result(self, prediction, confidence):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Prediction Result:", ln=True)
        self.set_font("Arial", "", 10)
        result = "Heart Disease" if prediction == 1 else "No Heart Disease"
        self.cell(0, 8, f"Result: {result}", ln=True)
        self.cell(0, 8, f"Confidence: {confidence:.2f}%", ln=True)

    def add_risk_explanation(self, prediction):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Risk Explanation:", ln=True)
        self.set_font("Arial", "", 10)
        if prediction == 1:
            self.multi_cell(0, 8, "\nBased on the inputs provided, the model indicates a higher likelihood of heart disease. It's important to follow up with a healthcare provider for further evaluation.")
        else:
            self.multi_cell(0, 8, "\nThe model predicts a low risk of heart disease. Continue maintaining a healthy lifestyle and consult healthcare professionals as needed.")

def generate_pdf_report(input_data, prediction, confidence):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_input_summary(input_data.to_dict(orient="records")[0])
    pdf.add_prediction_result(prediction, confidence)
    pdf.add_risk_explanation(prediction)

    temp_dir = tempfile.gettempdir()
    report_path = os.path.join(temp_dir, "heart_disease_report.pdf")
    pdf.output(report_path)
    return report_path

def show():
    st.title("🧾 Reports")

    if "prediction" not in st.session_state:
        st.warning("No prediction made yet! Please make a prediction first.")
        return

    pred = st.session_state.prediction
    confidence = st.session_state.confidence
    input_data = st.session_state.get("input_data")

    st.subheader("🩺 Prediction Summary")
    st.success(f"Prediction: {'Heart Disease' if pred == 1 else 'No Heart Disease'}")
    st.info(f"Confidence: {confidence:.2f}%")

    if input_data is not None:
        st.subheader("📊 Input Data")
        st.dataframe(input_data)

        if st.button("📄 Generate PDF Report"):
            pdf_path = generate_pdf_report(input_data, pred, confidence)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📅 Download Report as PDF",
                    data=f,
                    file_name="Heart_Disease_Report.pdf",
                    mime="application/pdf"
                )
