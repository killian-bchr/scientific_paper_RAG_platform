from typing import List

import streamlit as st
from constants import DefaultValues, Pages, SessionStateConstants
from utils import Utils

from database.tables import AuthorORM, CategoryORM, ChunkORM, DomainORM, PaperORM


class Components:
    @staticmethod
    def render_category_button(category: CategoryORM) -> None:
        label = f"{category.name}"

        if st.button(label, key=f"cat_{category.id}"):
            Utils.set_session_state(category.domain.name, SessionStateConstants.DOMAIN)
            Utils.set_session_state(category.name, SessionStateConstants.CATEGORY)

            Utils.switch_page(Pages.PAPERS)

    @staticmethod
    def render_category_buttons(categories: List[CategoryORM]) -> None:
        for category in categories:
            Components.render_category_button(category)

    @staticmethod
    def render_domain_button(domain: DomainORM) -> None:
        if st.button(domain.name, key=f"domain_{domain.id}"):
            Utils.set_session_state(domain.name, SessionStateConstants.DOMAIN)
            Utils.set_session_state(DefaultValues.ALL, SessionStateConstants.CATEGORY)

            Utils.switch_page(Pages.PAPERS)

    @staticmethod
    def render_domain_buttons(domains: List[DomainORM]) -> None:
        for domain in domains:
            Components.render_domain_button(domain)

    @staticmethod
    def render_authors_count(authors: List[AuthorORM]) -> None:
        st.write(f"Total authors: **{len(authors)}**")

    @staticmethod
    def render_authors(authors: List[AuthorORM]) -> None:
        for author in authors:
            st.write(f"- {author.name}")

    @staticmethod
    def select_chunk_type(chunks: List[ChunkORM]) -> str:
        chunk_types = Utils.extract_chunk_types(chunks)
        return st.selectbox("Filter by type", [DefaultValues.ALL] + chunk_types)

    @staticmethod
    def select_domains(domains: List[DomainORM], in_sidebar: bool = False) -> str:
        container = st.sidebar if in_sidebar else st

        options = [DefaultValues.ALL] + [d.name for d in domains]

        return container.selectbox(
            "Domain",
            options,
            key=SessionStateConstants.DOMAIN,
        )

    @staticmethod
    def select_categories(
        categories: List[CategoryORM], in_sidebar: bool = False
    ) -> str:
        container = st.sidebar if in_sidebar else st

        options = [DefaultValues.ALL] + [c.name for c in categories]

        return container.selectbox(
            "Category",
            options,
            key=SessionStateConstants.CATEGORY,
        )

    @staticmethod
    def select_start_year(in_sidebar: bool = False) -> int:
        container = st.sidebar if in_sidebar else st

        years = Utils.get_years_range()
        options = [DefaultValues.ALL] + years

        return container.selectbox(
            "Start year",
            options,
            key=SessionStateConstants.START_YEAR,
        )

    @staticmethod
    def select_end_year(in_sidebar: bool = False) -> int:
        container = st.sidebar if in_sidebar else st

        years = Utils.get_years_range()
        options = [DefaultValues.ALL] + years

        return container.selectbox(
            "End year",
            options,
            key=SessionStateConstants.END_YEAR,
        )

    @staticmethod
    def select_paper_title(papers: List[PaperORM]) -> str:
        paper_titles = Utils.create_papers_dict(papers)

        return st.selectbox("Select a paper", list(paper_titles.keys()))

    @staticmethod
    def render_chunk(chunk: ChunkORM, index: int) -> None:
        with st.expander(
            f"{index + 1}. {chunk.chunk_type} | page {chunk.page_no}",
            expanded=False,
        ):
            st.write(chunk.content)

    @staticmethod
    def render_chunks(chunks: List[ChunkORM]) -> None:
        for i, chunk in enumerate(chunks):
            Components.render_chunk(chunk, i)

    @staticmethod
    def render_chunks_button(paper: PaperORM) -> None:
        if st.button("🔎 View chunks"):
            Utils.set_session_state(paper.id, SessionStateConstants.PAPER_ID)
            Utils.set_session_state(paper.title, SessionStateConstants.PAPER_TITLE)
            Utils.switch_page(Pages.CHUNKS)

    @staticmethod
    def render_paper_button(paper: PaperORM) -> None:
        if st.button("🔍 View paper", key=f"view_{paper.id}"):
            Utils.set_session_state(paper.id, SessionStateConstants.PAPER_ID)
            Utils.set_session_state(False, SessionStateConstants.SEARCH_ACTIVE)
            Utils.switch_page(Pages.PAPERS)

    @staticmethod
    def render_pdf_link_button(paper: PaperORM) -> None:
        if not paper.pdf_url:
            return
        st.link_button(
            "📄 Open PDF",
            paper.pdf_url,
        )

    @staticmethod
    def render_clear_filters_button(in_sidebar: bool = False) -> None:
        container = st.sidebar if in_sidebar else st

        if container.button("🧹 Clear filters"):
            st.session_state.clear()
            st.rerun()

    @staticmethod
    def render_paper_details(paper: PaperORM) -> None:
        st.markdown(f"### {paper.title}")

        st.markdown("**Publication Date:** " + str(paper.publication_date))
        st.markdown("**Authors:** " + ", ".join(a.name for a in paper.authors))
        st.markdown("**Domains:** " + ", ".join(d.name for d in paper.domains))
        st.markdown("**Categories:** " + ", ".join(c.name for c in paper.categories))
