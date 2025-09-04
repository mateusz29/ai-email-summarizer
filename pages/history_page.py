import streamlit as st

from crud import get_all_summaries

st.title("📜 Summary History")
st.write("Here you can find all the email summaries you've generated in the past.")

summaries = get_all_summaries()

if not summaries:
    st.info("No summaries found. Go to the 'Summarize' page to create one!")
else:
    for summary in summaries:
        with st.container(border=True):
            col1, col2 = st.columns([7, 1])
            with col1:
                st.markdown(summary.summary)
            with col2:
                st.caption(f"Created on: {summary.created_at.strftime('%Y-%m-%d %H:%M')}")

            with st.expander("Show Original Email Text"):
                st.text(summary.email_text)
        st.write("")
