from datetime import date, datetime

import streamlit as st
from load_data import LoadData

from retriever.general_retriever import GeneralRetriever

DEFAULT_DOMAIN = "All"
DEFAULT_CATEGORY = "All"
DEFAULT_START_YEAR = "All"
DEFAULT_END_YEAR = "All"

st.session_state.setdefault("selected_domain", DEFAULT_DOMAIN)
st.session_state.setdefault("selected_category", DEFAULT_CATEGORY)
st.session_state.setdefault("start_year", DEFAULT_START_YEAR)
st.session_state.setdefault("end_year", DEFAULT_END_YEAR)

st.title("🔍 Search")

domains = LoadData.load_domains()
categories = LoadData.load_categories()

current_year = datetime.now().year
years = list(range(1970, current_year + 1))

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        selected_domain = st.selectbox(
            "Domain",
            ["All"] + [d.name for d in domains],
            key="selected_domain",
        )

    with col2:
        selected_category = st.selectbox(
            "Category",
            ["All"] + [c.name for c in categories],
            key="selected_category",
        )

    with col3:
        start_year = st.selectbox(
            "Start year",
            ["All"] + years,
            key="start_year",
        )

    with col4:
        end_year = st.selectbox(
            "End year",
            ["All"] + years,
            key="end_year",
        )

if st.button("🧹 Clear filters"):
    st.session_state.clear()
    st.rerun()

start_date, end_date = None, None

if start_year != "All":
    start_date = date(start_year, 1, 1)

if end_year != "All":
    end_date = date(end_year, 12, 31)

if start_date and end_date and start_date > end_date:
    st.sidebar.error("Start year must be before end year")
    st.stop()

papers = LoadData.load_papers(start_date, end_date)


def paper_matches_filters(paper):
    if selected_domain != "All":
        if selected_domain not in [d.name for d in paper.domains]:
            return False
    if selected_category != "All":
        if selected_category not in [c.name for c in paper.categories]:
            return False
    return True


filtered_papers = [p for p in papers if paper_matches_filters(p)]

st.markdown("## 🧠 Query")

with st.container():
    col_query, col_btn = st.columns([5, 1])

    with col_query:
        query = st.text_input(
            "Search papers",
            placeholder="e.g. prompt optimization for LLMs",
            label_visibility="collapsed",
        )

    with col_btn:
        search_clicked = st.button("🔍 Search")

if search_clicked:
    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()

    if not filtered_papers:
        st.warning("No paper matches the selected filters.")
        st.stop()

    retriever = GeneralRetriever(filtered_papers)

    ranked_ids = retriever.top_k_papers(query, k=10)

    st.markdown("## 📄 Results")

    for paper_id in ranked_ids:
        paper = next(p for p in filtered_papers if p.id == paper_id)

        with st.container():
            st.markdown(f"### {paper.title}")

            st.markdown(
                f"**Authors: ** {', '.join(a.name for a in paper.authors)}  \n"
                f"**Domains: ** {', '.join(d.name for d in paper.domains)}  \n"
                f"**Categories: ** {', '.join(c.name for c in paper.categories)}"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("🔍 View paper", key=f"view_{paper.id}"):
                    st.session_state["selected_paper_id"] = paper.id
                    st.switch_page("pages/papers.py")

            with col2:
                if paper.pdf_url:
                    st.link_button(
                        "📄 Open PDF",
                        paper.pdf_url,
                    )

            st.divider()
