from datetime import date
from typing import List, Optional

import streamlit as st

from database.session import get_session
from database.tables import AuthorORM, CategoryORM, ChunkORM, DomainORM, PaperORM
from helpers.utils import Utils
from retriever.general_retriever import GeneralRetriever


class LoadData:
    @staticmethod
    @st.cache_data
    def load_authors() -> List[AuthorORM]:
        with get_session() as session:
            return Utils.fetch_all_authors(session)

    @staticmethod
    @st.cache_data
    def load_domains() -> List[DomainORM]:
        with get_session() as session:
            return Utils.fetch_all_domains(session)

    @staticmethod
    @st.cache_data
    def load_categories() -> List[CategoryORM]:
        with get_session() as session:
            return Utils.fetch_all_categories(session)

    @staticmethod
    @st.cache_data
    def load_papers(
        start_date: Optional[date], end_date: Optional[date]
    ) -> List[PaperORM]:
        with get_session() as session:
            return Utils.fetch_papers_by_period(session, start_date, end_date)

    @staticmethod
    @st.cache_data
    def load_chunks_by_paper_id(paper_id: int) -> List[ChunkORM]:
        with get_session() as session:
            return Utils.fetch_chunks_by_paper_id(session, paper_id)

    @staticmethod
    @st.cache_resource
    def load_retriever(papers: List[PaperORM]) -> GeneralRetriever:
        return GeneralRetriever(papers)
