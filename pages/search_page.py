import streamlit as st

from crud import search_summaries

st.title("🔎 Search")
st.write("Search through your past email summaries.")

with st.form(key="search_form", border=False):
    keyword_query = st.text_input(
        "Enter keyword",
        placeholder="Search in summary ...",
    )

    search_button = st.form_submit_button("Search", type="primary")

if search_button:
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
