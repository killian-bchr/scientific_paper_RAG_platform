import streamlit as st

from load_data import LoadData


st.title("🌐 Domains")

domains = LoadData.load_domains()

for domain in domains:
    if st.button(domain.name, key=f"domain_{domain.id}"):
        st.session_state["selected_domain"] = domain.name
        st.session_state["selected_category"] = "All"

        st.switch_page("pages/papers.py")
