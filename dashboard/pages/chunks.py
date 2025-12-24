import streamlit as st

from load_data import LoadData


st.title("📦 Chunks")

if "selected_paper_id" not in st.session_state:
    st.warning("No paper selected.")
    st.stop()

paper_id = st.session_state["selected_paper_id"]
paper_title = st.session_state.get("selected_paper_title", "")

st.subheader(f"📄 {paper_title}")

chunks = LoadData.load_chunks_by_paper_id(paper_id)

chunk_types = sorted(set(c.chunk_type for c in chunks))
selected_type = st.selectbox("Filter by type", ["All"] + chunk_types)

if selected_type != "All":
    chunks = [c for c in chunks if c.chunk_type == selected_type]

st.metric("📦 Number of chunks", len(chunks))

for i, chunk in enumerate(chunks):
    with st.expander(
        f"{i+1}. {chunk.chunk_type} | page {chunk.page_no}",
        expanded=False
    ):
        st.write(chunk.content)
