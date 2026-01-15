import streamlit as st
from components import Components
from load_data import LoadData
from service import Service
from session_state import init_session_state

init_session_state()

st.title("📄 Papers")

domains = LoadData.load_domains()
categories = LoadData.load_categories()

Components.render_clear_filters_button(in_sidebar=True)

st.sidebar.header("🔍 Filters")

selected_domain = Components.select_domains(domains, in_sidebar=True)
selected_category = Components.select_categories(categories, in_sidebar=True)

st.sidebar.header("📅 Publication period")

start_year = Components.select_start_year(in_sidebar=True)
end_year = Components.select_end_year(in_sidebar=True)
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

Components.render_paper_details(paper)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        Components.render_chunks_button(paper)

    with col2:
        Components.render_pdf_link_button(paper)

st.markdown("### 📝 Abstract")
st.write(paper.abstract)
