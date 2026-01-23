import streamlit as st
from components import Components
from constants import SessionStateConstants
from load_data import LoadData
from service import Service
from session_state import init_session_state

init_session_state()

st.title("🔍 Search")

domains = LoadData.load_domains()
categories = LoadData.load_categories()

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        selected_domain = Components.select_domains(domains)

    with col2:
        selected_category = Components.select_categories(categories)

    with col3:
        start_year = Components.select_start_year()

    with col4:
        end_year = Components.select_end_year()

Components.render_clear_filters_button()

start_date, end_date = Service.compute_start_and_end_date(start_year, end_year)

papers = LoadData.load_papers(start_date, end_date)

filtered_papers = Service.filter_papers(
    papers,
    selected_domain,
    selected_category,
)

st.markdown("## 🧠 Query")

with st.container():
    col_query, col_btn = st.columns([5, 1])
    warning_placeholder = st.empty()

    with col_query:
        query = st.text_input(
            "Search papers",
            placeholder="e.g. prompt optimization for LLMs",
            label_visibility="collapsed",
        )

    with col_btn:
        if st.button("🔍 Search"):
            if not query.strip():
                warning_placeholder.warning("Please enter a query.")
                st.session_state[SessionStateConstants.SEARCH_ACTIVE] = False
                st.stop()

            st.session_state[SessionStateConstants.SEARCH_ACTIVE] = True

if st.session_state.get(SessionStateConstants.SEARCH_ACTIVE, False):
    if not filtered_papers:
        st.warning("No paper matches the selected filters.")
        st.stop()

    ranked_ids = Service.retrieve_top_k_papers(filtered_papers, query)

    st.markdown("## 📄 Results")

    for paper_id in ranked_ids:
        paper = next(p for p in filtered_papers if p.id == paper_id)

        with st.container():
            Components.render_paper_details(paper)

            col1, col2 = st.columns(2)

            with col1:
                Components.render_paper_button(paper)

            with col2:
                Components.render_pdf_link_button(paper)

            st.divider()
