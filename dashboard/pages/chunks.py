import streamlit as st
from components import Components
from constants import SessionStateConstants
from load_data import LoadData
from service import Service
from session_state import init_session_state

init_session_state()

st.title("📦 Chunks")

if SessionStateConstants.PAPER_ID not in st.session_state:
    st.warning("No paper selected.")
    st.stop()

paper_id = st.session_state[SessionStateConstants.PAPER_ID]
paper_title = st.session_state.get(SessionStateConstants.PAPER_TITLE, "")

st.subheader(f"📄 {paper_title}")

chunks = LoadData.load_chunks_by_paper_id(paper_id)

selected_chunk_type = Components.select_chunk_type(chunks)

chunks = Service.filter_chunks_by_type(chunks, selected_chunk_type)

st.metric("📦 Number of chunks", len(chunks))

Components.render_chunks(chunks)
