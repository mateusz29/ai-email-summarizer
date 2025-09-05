from sqlalchemy import select

from database import get_session
from models import EmailSummary


def save_email_summary(email_text: str, summary: str) -> None:
    with get_session() as session:
        new_summary = EmailSummary(email_text=email_text, summary=summary)
        session.add(new_summary)
        session.commit()


def get_all_summaries():
    with get_session() as session:
        statement = select(EmailSummary).order_by(EmailSummary.created_at.desc())
        result = session.execute(statement).scalars().all()
        return result


def search_summaries(keyword: str):
    with get_session() as session:
        statement = (
            select(EmailSummary)
            .where(EmailSummary.summary.ilike(f"%{keyword}%"))
            .order_by(EmailSummary.created_at.desc())
        )
        result = session.execute(statement).scalars().all()
        return result
