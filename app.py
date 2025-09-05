import streamlit as st

st.set_page_config(page_title="AI Email Summarizer", page_icon="📧", layout="wide")

pages = [
    st.Page("pages/summarize_page.py", title="Summarize", icon="📧", default=True),
    st.Page("pages/history_page.py", title="History", icon="📜"),
    st.Page("pages/search_page.py", title="Search", icon="🔎"),
]

pg = st.navigation(pages)
pg.run()
