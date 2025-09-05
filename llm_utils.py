import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from crud import save_email_summary

load_dotenv()

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")


def get_email_summary(email_text: str, length: str, use_bulletpoints: bool, analyze_sentiment: bool) -> str:
    if not email_text:
        return "Error: No email text provided."

    instructions = ["You are a highly-skilled assistant that summarizes emails efficiently."]

    length_instruction_map = {
        "short": "Generate a very brief, one-sentence summary.",
        "medium": "Generate a concise, one-paragraph summary.",
        "long": "Generate a detailed summary covering all key points.",
    }
    instructions.append(length_instruction_map.get(length, length_instruction_map["medium"]))

    if use_bulletpoints:
        instructions.append("Use bullet points to list key topics, questions, or action items.")

    if analyze_sentiment:
        instructions.append(
            "After the summary, add a new section on a new line starting with 'Sentiment:' "
            "followed by the email's perceived tone (e.g., Positive, Neutral, Negative) and a brief justification."
        )

    instructions.append(
        "Always start your summary with 'This email is about'. "
        "Do not include any other commentary or headers unless explicitly asked for (like 'Sentiment:')."
    )

    final_instructions = " ".join(instructions)

    try:
        response = client.responses.create(
            model="gpt-5-nano",
            instructions=final_instructions,
            input=email_text,
        )
        summary = response.output_text

        save_email_summary(email_text, summary)

        return summary
    except Exception as e:
        st.error(f"An error accured: {e}")
        return None
