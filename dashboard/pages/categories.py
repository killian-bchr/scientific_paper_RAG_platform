import streamlit as st
from components import Components
from load_data import LoadData

st.title("🧩 Categories")

categories = LoadData.load_categories()

Components.render_category_buttons(categories)
