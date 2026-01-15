import streamlit as st
from components import Components
from load_data import LoadData
from session_state import init_session_state

init_session_state()

st.title("🧩 Categories")

categories = LoadData.load_categories()

Components.render_category_buttons(categories)
