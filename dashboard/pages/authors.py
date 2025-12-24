import streamlit as st

from load_data import LoadData


st.title("👤 Authors")

authors = LoadData.load_authors()

st.write(f"Total authors: **{len(authors)}**")

for author in authors:
    st.write(f"- {author.name}")
