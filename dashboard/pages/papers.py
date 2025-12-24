from datetime import date, datetime

import streamlit as st
from load_data import LoadData

st.title("📄 Papers")

domains = LoadData.load_domains()
categories = LoadData.load_categories()

st.sidebar.header("🔍 Filters")

if "selected_domain" not in st.session_state:
    st.session_state.selected_domain = "All"

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

selected_domain = st.sidebar.selectbox(
    "Domain",
    ["All"] + [d.name for d in domains],
    index=(["All"] + [d.name for d in domains]).index(
        st.session_state["selected_domain"]
    ),
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + [c.name for c in categories],
    index=(["All"] + [c.name for c in categories]).index(
        st.session_state["selected_category"]
    ),
)

current_year = datetime.now().year
years = list(range(1970, current_year + 1))

st.sidebar.header("📅 Publication period")

start_year = st.sidebar.selectbox("Start year", ["All"] + years, index=0)

end_year = st.sidebar.selectbox("End year", ["All"] + years, index=len(years))

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

if not filtered_papers:
    st.warning("No paper matches the selected filters.")
    st.stop()

paper_titles = {p.title: p for p in filtered_papers}

selected_title = st.selectbox("Select a paper", list(paper_titles.keys()))

paper = paper_titles[selected_title]

st.markdown("## 📌 Paper Details")

st.markdown(f"### {paper.title}")

st.markdown("**Publication Date:** " + str(paper.publication_date))
st.markdown("**Authors:** " + ", ".join(a.name for a in paper.authors))
st.markdown("**Domains:** " + ", ".join(d.name for d in paper.domains))
st.markdown("**Categories:** " + ", ".join(c.name for c in paper.categories))


if st.button("🔎 View chunks"):
    st.session_state["selected_paper_id"] = paper.id
    st.session_state["selected_paper_title"] = paper.title
    st.switch_page("pages/chunks.py")

st.markdown("### 📝 Abstract")
st.write(paper.abstract)
