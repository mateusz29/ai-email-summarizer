from sqlalchemy import func, select

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


def get_summaries(skip: int = 0, limit: int = 5):
    with get_session() as session:
        statement_data = select(EmailSummary).order_by(EmailSummary.created_at.desc()).offset(skip).limit(limit)
        summaries = session.execute(statement_data).scalars().all()

        statement_count = select(func.count()).select_from(EmailSummary)
        total_count = session.execute(statement_count).scalar_one()
        return summaries, total_count


def search_summaries(keyword: str, skip: int = 0, limit: int = 5):
    with get_session() as session:
        base_query = select(EmailSummary).where(EmailSummary.summary.ilike(f"%{keyword}%"))

        statement_data = base_query.order_by(EmailSummary.created_at.desc()).offset(skip).limit(limit)
        summaries = session.execute(statement_data).scalars().all()

        statement_count = select(func.count()).select_from(base_query.subquery())
        total_count = session.execute(statement_count).scalar_one()
        return summaries, total_count
