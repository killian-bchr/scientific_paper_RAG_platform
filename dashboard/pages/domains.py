import streamlit as st
from components import Components
from load_data import LoadData

st.title("🌐 Domains")

domains = LoadData.load_domains()

Components.render_domain_buttons(domains)
