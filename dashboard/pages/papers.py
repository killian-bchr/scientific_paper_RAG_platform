import streamlit as st
from components import Components
from constants import DefaultValues, SessionStateConstants
from load_data import LoadData
from service import Service

st.title("📄 Papers")

domains = LoadData.load_domains()
categories = LoadData.load_categories()

if st.sidebar.button("🧹 Clear filters"):
    st.session_state.clear()
    st.rerun()

st.sidebar.header("🔍 Filters")

if SessionStateConstants.DOMAIN not in st.session_state:
    st.session_state[SessionStateConstants.DOMAIN] = DefaultValues.ALL

if SessionStateConstants.CATEGORY not in st.session_state:
    st.session_state[SessionStateConstants.CATEGORY] = DefaultValues.ALL

selected_domain = Components.select_domains(domains)
selected_category = Components.select_categories(categories)

st.sidebar.header("📅 Publication period")

start_year, end_year = Components.select_start_and_end_year()
start_date, end_date = Service.compute_start_and_end_date(start_year, end_year)

papers = LoadData.load_papers(start_date, end_date)

filtered_papers = Service.filter_papers(
    papers,
    selected_domain,
    selected_category,
)

if not filtered_papers:
    st.warning("No paper matches the selected filters.")
    st.stop()

selected_title = Components.select_paper_title(filtered_papers)

paper = Service.fetch_paper_selected(filtered_papers, selected_title)

st.markdown("## 📌 Paper Details")

st.markdown(f"### {paper.title}")

st.markdown("**Publication Date:** " + str(paper.publication_date))
st.markdown("**Authors:** " + ", ".join(a.name for a in paper.authors))
st.markdown("**Domains:** " + ", ".join(d.name for d in paper.domains))
st.markdown("**Categories:** " + ", ".join(c.name for c in paper.categories))

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        Components.render_chunks_button(paper)

    with col2:
        Components.render_pdf_link_button(paper)

st.markdown("### 📝 Abstract")
st.write(paper.abstract)
