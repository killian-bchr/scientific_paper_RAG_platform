import streamlit as st
from components import Components
from load_data import LoadData

st.title("👤 Authors")

authors = LoadData.load_authors()

Components.render_authors_count(authors)
Components.render_authors(authors)
