import streamlit as st

from utils import get_email_summary

st.title("📧 AI Email Summarizer")
st.write("Paste the full content of an email below and click 'Summarize' to get a quick overview.")

st.header("Paste Your Email Here:")
email_input = st.text_area(label="Email Content", height=300, label_visibility="collapsed")

if st.button("Summarize Email", type="primary"):
    if email_input.strip():
        with st.spinner("Analyzing and summarizing your email..."):
            summary = get_email_summary(email_input)
            if summary:
                st.header("📄 Summary:")
                st.markdown(summary)
    else:
        st.warning("Please paste an email into the text box above.")
