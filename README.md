# Heart Disease Prediction Web App

A Streamlit-based web application for predicting the likelihood of heart disease using a trained machine learning model. The app allows users to explore health data, enter patient details, view predictions, and generate a downloadable report.

## Features

- Interactive dashboard with multiple pages
- Heart disease risk prediction from user input
- Data insights and exploration views
- Model training interface with multiple classifiers
- PDF report generation for prediction summaries
- Progress and learning resources for heart health awareness

## Project Structure

- `app.py` – Main Streamlit entry point
- `pg/` – Page modules for Home, Insights, Prediction, Reports, Learn More, About, Model Training, and Progress
- `utils/` – Preprocessing and model utilities
- `data/` – Dataset files used for training and exploration
- `reports/` and `generated_reports/` – Saved report outputs
- `assests/` – Images and static assets

## Technologies Used

- Python
- Streamlit
- pandas
- scikit-learn
- joblib
- matplotlib
- seaborn
- Pillow
- fpdf

## Installation

1. Clone or open the project folder.
2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install streamlit streamlit-option-menu pandas scikit-learn joblib pillow matplotlib seaborn fpdf
```

## Running the App

From the project root, run:

```bash
streamlit run app.py
```

The app will open in your browser.

## Usage

- Open the Home page to understand the project
- Use the Prediction page to enter health details and get a risk estimate
- Visit the Reports page to download a PDF summary
- Use the Train Model page to train and save your own classifier

## Notes

- The prediction flow expects trained model files named `heart_disease_rf_model.pkl` and `heart_disease_scaler.pkl` in the project root.
- If those files are missing, you can train a model from the app and save it, or place the required model files in the correct location before running predictions.

## License

This project is intended for educational and demonstration purposes.
