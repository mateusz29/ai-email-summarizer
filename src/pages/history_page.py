import streamlit as st

from constants import PAGE_SIZE
from database.crud import get_summaries
from ui.components import display_pagination_controls

st.title("📜 Summary History")
st.write("Here you can find all the email summaries you've generated in the past.")

if "page_num" not in st.session_state:
    st.session_state.page_num = 1

skip = (st.session_state.page_num - 1) * PAGE_SIZE

summaries, total_summaries = get_summaries(skip=skip, limit=PAGE_SIZE)

if not summaries:
    st.info("No summaries found. Go to the 'Summarize' page to create one!")
else:
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
