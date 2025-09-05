import streamlit as st

from llm_utils import get_email_summary

st.title("📧 AI Email Summarizer")
st.write("Paste an email below, choose your summarization options, and get a quick overview in seconds.")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Paste Your Email Here:")
    email_input = st.text_area(label="Email Content", height=300, label_visibility="collapsed")

with col2:
    st.header("Customization Options")

    summary_length = st.radio(
        "Select Summary Length:",
        options=["Short", "Medium", "Long"],
        index=1,
        horizontal=True,
    )
    use_bulletpoints = st.checkbox("Use bullet points for key topics")
    include_sentiment = st.checkbox("Include sentiment analysis")

if st.button("✨ Summarize Email", type="primary"):
    if email_input.strip():
        with st.spinner("🧠 Analyzing and summarizing your email..."):
            summary = get_email_summary(
                email_text=email_input,
                length=summary_length.lower(),
                use_bulletpoints=use_bulletpoints,
                analyze_sentiment=include_sentiment,
            )
            if summary:
                st.header("📄 Summary:")
                st.markdown(summary)
    else:
        st.warning("Please paste an email into the text box above.")
