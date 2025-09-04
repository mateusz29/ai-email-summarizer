import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from crud import save_email_summary

load_dotenv()

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")


def get_email_summary(email_text: str) -> str:
    if not email_text:
        return "Error: No email text provided."

    try:
        response = client.responses.create(
            model="gpt-5-nano",
            instructions=(
                "You are a highly-skilled assistant that summarizes emails efficiently. "
                "Always start your summary with 'This email is about' and then briefly describe the content. "
                "Do not include any additional commentary or information."
            ),
            input=email_text,
        )
        summary = response.output_text

        save_email_summary(email_text, summary)

        return summary
    except Exception as e:
        st.error(f"An error accured: {e}")
        return None


def main():
    st.set_page_config(page_title="AI Email Summarizer", layout="wide")

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


if __name__ == "__main__":
    main()
