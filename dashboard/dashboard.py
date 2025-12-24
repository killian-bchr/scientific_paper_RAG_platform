import streamlit as st

from database.session import get_session
from helpers.utils import Utils

st.set_page_config(page_title="Paper DB", layout="wide")

st.title("📚 Paper Database Dashboard")

if "view" not in st.session_state:
    st.session_state.view = "home"

with get_session() as session:
    n_papers = Utils.count_papers(session)
    n_authors = Utils.count_authors(session)
    n_domains = Utils.count_domains(session)
    n_categories = Utils.count_categories(session)

col1, col2, col3, col4 = st.columns(4)

col1.metric("📄 Papers", n_papers)
col2.metric("👤 Authors", n_authors)
col3.metric("🏷️ Domains", n_domains)
col4.metric("📂 Categories", n_categories)

st.info("⬅️ Use the sidebar to navigate")
