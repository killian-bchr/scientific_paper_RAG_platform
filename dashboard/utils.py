from datetime import datetime
from typing import Dict, List

import streamlit as st
from constants import Pages, SessionStateConstants

from backend.database.tables import ChunkORM, PaperORM


class Utils:
    @staticmethod
    def switch_page(page: Pages) -> None:
        st.switch_page(page)

    @staticmethod
    def set_session_state(
        value: str,
        session_state: SessionStateConstants,
    ) -> None:
        st.session_state[session_state] = value

    @staticmethod
    def extract_chunk_types(chunks: List[ChunkORM]) -> List[str]:
        return sorted(set(c.chunk_type for c in chunks))

    @staticmethod
    def get_years_range() -> List[int]:
        current_year = datetime.now().year
        return list(range(1970, current_year + 1))

    @staticmethod
    def create_papers_dict(papers: List[PaperORM]) -> Dict[str, PaperORM]:
        return {p.title: p for p in papers}
