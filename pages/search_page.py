import streamlit as st

from crud import search_summaries


def search_callback():
    if st.session_state.keyword_input:
        st.session_state.search_clicked = True


st.title("🔎 Search")
st.write("Search through your past email summaries.")

st.text_input("Enter keyword", placeholder="Search in summary ...", key="keyword_input", on_change=search_callback)

if st.button("Search", type="primary") or st.session_state.get("search_clicked", False):
    st.session_state.search_clicked = False

    keyword_query = st.session_state.keyword_input

    if keyword_query:
        summaries = search_summaries(keyword=keyword_query)

        if summaries:
            st.write(f"Found **{len(summaries)}** matching summaries.")
            st.write("")

            for summary in summaries:
                with st.container(border=True):
                    col1, col2 = st.columns([7, 1])
                    with col1:
                        st.markdown(summary.summary)
                    with col2:
                        st.caption(f"Created on: {summary.created_at.strftime('%Y-%m-%d %H:%M')}")

                    with st.expander("Show Original Email Text"):
                        st.code(summary.email_text, language="text")

                st.write("")
        else:
            st.warning("No summaries found matching your search criteria.")

    else:
        st.info("Please enter a keyword to search the summaries.")
