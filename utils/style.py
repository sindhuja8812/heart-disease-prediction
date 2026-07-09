import streamlit as st

# Color Palette
PRIMARY_COLOR = "#cab7bf"  # Cold Turkey
SECONDARY_COLOR = "#8c4a4d"  # Copper Rust
BACKGROUND_COLOR = "#38363c"  # Ship Gray
ACCENT_COLOR = "#a86456"  # Matrix
TEXT_COLOR = "#ffffff"

# Apply custom CSS
def apply_custom_css():
    st.markdown(
        f"""
        <style>
            body {{
                background-color: {BACKGROUND_COLOR};
                color: {TEXT_COLOR};
            }}
            .stButton > button {{
                background-color: {PRIMARY_COLOR};
                color: black;
                border-radius: 8px;
                font-size: 16px;
            }}
            .stTextInput > div > div > input {{
                background-color: {SECONDARY_COLOR};
                color: white;
            }}
            .stSelectbox > div {{
                background-color: {PRIMARY_COLOR};
                color: black;
            }}
        </style>
        """, 
        unsafe_allow_html=True
    )

# Sidebar Menu Style
def menu_style():
    return {
        "container": {"background-color": BACKGROUND_COLOR},
        "icon": {"color": TEXT_COLOR, "font-size": "18px"},
        "nav-link": {
            "color": TEXT_COLOR, 
            "font-size": "16px", 
            "text-align": "left", 
            "margin": "5px",
        },
        "nav-link-selected": {"background-color": ACCENT_COLOR, "color": "white"},
    }
