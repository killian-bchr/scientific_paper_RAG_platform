import streamlit as st
from components import Components
from load_data import LoadData
from session_state import init_session_state

init_session_state()

st.title("👤 Authors")

authors = LoadData.load_authors()

Components.render_authors_count(authors)
Components.render_authors(authors)
