import streamlit as st

from constants import PAGE_SIZE
from database.crud import search_summaries
from ui.components import display_pagination_controls

st.title("🔎 Search")
st.write("Search through your past email summaries.")

if "page_num" not in st.session_state:
    st.session_state.page_num = 1
if "search_keyword" not in st.session_state:
    st.session_state.search_keyword = ""

with st.form(key="search_form", border=False):
    keyword_query = st.text_input(
        "Enter keyword", placeholder="Search in summary ...", value=st.session_state.search_keyword
    )

    if st.form_submit_button("Search", type="primary"):
        st.session_state.search_keyword = keyword_query
        st.session_state.page_num = 1
        st.rerun()

if st.session_state.search_keyword:
    skip = (st.session_state.page_num - 1) * PAGE_SIZE

    summaries, total_summaries = search_summaries(keyword=keyword_query, skip=skip, limit=PAGE_SIZE)

    if summaries:
        st.write(f"Showing **{len(summaries)}** of **{total_summaries}** summaries.")

        for summary in summaries:
            with st.container(border=True):
                col1, col2 = st.columns([7, 1])
                with col1:
                    st.markdown(summary.summary)
                with col2:
                    st.caption(f"Created on: {summary.created_at.strftime('%Y-%m-%d %H:%M')}")

                with st.expander("Show Original Email Text"):
                    st.markdown(summary.email_text)
            st.write("")

        display_pagination_controls(total_items=total_summaries, page_size=PAGE_SIZE)
    else:
        st.warning("No summaries found matching your search criteria.")
else:
    st.info("Please enter a keyword to search the summaries.")
