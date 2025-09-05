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
