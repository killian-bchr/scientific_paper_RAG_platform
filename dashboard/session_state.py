import streamlit as st
from constants import DefaultValues, SessionStateConstants


def init_session_state() -> None:
    st.session_state.setdefault(SessionStateConstants.DOMAIN, DefaultValues.ALL)
    st.session_state.setdefault(SessionStateConstants.CATEGORY, DefaultValues.ALL)
    st.session_state.setdefault(SessionStateConstants.START_YEAR, DefaultValues.ALL)
    st.session_state.setdefault(SessionStateConstants.END_YEAR, DefaultValues.END_YEAR)
    st.session_state.setdefault(SessionStateConstants.SEARCH_ACTIVE, False)
