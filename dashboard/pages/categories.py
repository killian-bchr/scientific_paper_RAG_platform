import streamlit as st

from load_data import LoadData


st.title("🧩 Categories")

categories = LoadData.load_categories()

for category in categories:
    label = f"{category.name}"

    if st.button(label, key=f"cat_{category.id}"):
        st.session_state["selected_domain"] = category.domain.name
        st.session_state["selected_category"] = category.name

        st.switch_page("pages/papers.py")
