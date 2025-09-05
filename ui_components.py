import math

import streamlit as st


def display_pagination_controls(total_items: int, page_size: int):
    total_pages = math.ceil(total_items / page_size) if total_items > 0 else 1

    if total_pages <= 1:
        return

    st.write("---")

    def prev_page():
        st.session_state.page_num -= 1

    def next_page():
        st.session_state.page_num += 1

    _, prev_col, page_col, next_col, _ = st.columns([4, 2, 2, 2, 3])

    with prev_col:
        st.button("⬅️ Previous", on_click=prev_page, disabled=(st.session_state.page_num <= 1))

    with page_col:
        st.write(f"Page **{st.session_state.page_num}** of **{total_pages}**")

    with next_col:
        st.button("Next ➡️", on_click=next_page, disabled=(st.session_state.page_num >= total_pages))
