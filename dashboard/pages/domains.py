import streamlit as st
from components import Components
from load_data import LoadData
from session_state import init_session_state

init_session_state()

st.title("🌐 Domains")

domains = LoadData.load_domains()

Components.render_domain_buttons(domains)
