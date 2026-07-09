# --- app.py (Main Launcher) ---
import streamlit as st
from streamlit_option_menu import option_menu
import pg.home as home
import pg.insights as insights
import pg.prediction as prediction
import pg.reports as reports
import pg.learnmore as learnmore
import pg.about as about
import pg.model_trainer as model_trainer
import pg.progress as progress
import utils.style as style

# Set page config
st.set_page_config(page_title="Heart Disease Prediction", page_icon="", layout="wide")
style.apply_custom_css()

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Heart Disease Prediction",
        ["🏠 Home", "📊 Data Insights", "🔍 Prediction", "📅 Reports", "📖 Learn More", "🧠 Train Model", "📈 Track Progress","📘 About Project"],
        icons=["house", "bar-chart", "search", "folder", "book", "cpu", "activity", "info-circle"],
        menu_icon="heart",
        default_index=0,
        styles=style.menu_style()
    )

# Route Pages
if selected == "🏠 Home":
    home.show()
elif selected == "📊 Data Insights":
    insights.show()
elif selected == "🔍 Prediction":
    prediction.show()
elif selected == "📅 Reports":
    if st.session_state.get('prediction_made', True):
        reports.show()
    else:
        st.warning("No prediction made yet! Please make a prediction first.")
elif selected == "📖 Learn More":
    learnmore.show()
elif selected == "🧠 Train Model":
    model_trainer.show()
elif selected == "📘 About Project":
    about.show()
elif selected == "📈 Track Progress":
    progress.show()