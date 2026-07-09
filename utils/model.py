import joblib
import numpy as np

MODEL_PATH = "heart_disease_rf_model.pkl"
SCALER_PATH = "heart_disease_scaler.pkl"

def load_model():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler

def get_prediction(processed_input):
    model, _ = load_model()
    probas = model.predict_proba(processed_input)
    prediction = np.argmax(probas, axis=1)[0]
    confidence = np.max(probas, axis=1)[0] * 100
    return prediction, confidence