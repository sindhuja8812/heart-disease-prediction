import pandas as pd
from sklearn.preprocessing import StandardScaler

DATA_PATH = "data/heart_disease_cleaned.csv"

ENCODINGS = {
    'sex': {'Male': 0, 'Female': 1},
    'cp': {
        'Typical Angina': 0,
        'Asymptomatic': 1,
        'Non-anginal Pain': 2,
        'Atypical Angina': 3
    },
    'restecg': {
        'Left Ventricular Hypertrophy': 0,
        'Normal': 1,
        'ST-T Wave Abnormality': 2
    },
    'slope': {
        'Downsloping': 0,
        'Flat': 1,
        'Upsloping': 2
    },
    'thal': {
        'Fixed Defect': 0,
        'Normal': 1,
        'Reversible Defect': 2
    }
}

LABEL_COLS = list(ENCODINGS.keys())

def load_data(path=DATA_PATH):
    return pd.read_csv(path)

def preprocess_input(input_df, scaler):
    df = input_df.copy()

    for col in LABEL_COLS:
        df[col] = df[col].map(ENCODINGS[col])

    df['fbs'] = df['fbs'].astype(int)
    df['exang'] = df['exang'].astype(int)

    return scaler.transform(df)
